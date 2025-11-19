import sqlite3
import os
import re

# caminho simples do arquivo SQLite no mesmo diretório do projeto
DB_FILE = os.path.join(os.path.dirname(__file__), 'petshop.db')


class CursorContext:
  """Wrapper para cursor que fornece suporte a `with conn.cursor() as cursor`.
  Também converte placeholders `%s` para `?` do sqlite3 e emula `RETURNING`
  retornando `lastrowid` via `fetchone()` quando apropriado.
  """
  def __init__(self, real_cursor):
    self._cur = real_cursor
    self._returning = False
    self._lastrow = None

  def __enter__(self):
    return self

  def __exit__(self, exc_type, exc, tb):
    try:
      self._cur.close()
    except Exception:
      pass

  def execute(self, sql, params=None):
    # detectar cláusula RETURNING e removê-la (sqlite terá lastrowid)
    m = re.search(r"\bRETURNING\b.*$", sql, flags=re.IGNORECASE)
    if m:
      sql = sql[:m.start()].strip()
      self._returning = True
    # converter placeholders %s -> ?
    sql_transformed = sql.replace('%s', '?')
    if params is None:
      result = self._cur.execute(sql_transformed)
    else:
      result = self._cur.execute(sql_transformed, params)
    try:
      self._lastrow = self._cur.lastrowid
    except Exception:
      self._lastrow = None
    return result

  def fetchone(self):
    if self._returning:
      return (self._lastrow,)
    return self._cur.fetchone()

  def fetchall(self):
    return self._cur.fetchall()

  @property
  def rowcount(self):
    return self._cur.rowcount


class SQLiteConnectionWrapper:
  """Wrapper que expõe métodos compatíveis com o código existente (commit, rollback, close)
  e provê `cursor()` que pode ser usado como contexto (`with conn.cursor() as cursor`).
  """
  def __init__(self, conn):
    self._conn = conn

  def cursor(self):
    return CursorContext(self._conn.cursor())

  def commit(self):
    return self._conn.commit()

  def rollback(self):
    # sqlite3 não implementa rollback se não houver transação aberta,
    # mas chamamos para compatibilidade
    try:
      return self._conn.rollback()
    except Exception:
      pass

  def close(self):
    return self._conn.close()


def _init_db(conn_wrapper):
  """Cria as tabelas `clientes` e `funcionarios` se não existirem."""
  sql_clientes = (
    "CREATE TABLE IF NOT EXISTS clientes ("
    "cliente_id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "nome TEXT NOT NULL, telefone TEXT, email TEXT"
    ")"
  )
  sql_funcionarios = (
    "CREATE TABLE IF NOT EXISTS funcionarios ("
    "funcionario_id INTEGER PRIMARY KEY AUTOINCREMENT, "
    "nome TEXT NOT NULL, cargo TEXT, salario REAL"
    ")"
  )
  with conn_wrapper.cursor() as cur:
    cur.execute(sql_clientes)
    cur.execute(sql_funcionarios)
  conn_wrapper.commit()


def conectar():
  """Conecta (ou cria) um banco SQLite e retorna um wrapper compatível.
  Retorna None somente em erro crítico.
  """
  try:
    conn = sqlite3.connect(DB_FILE)
    wrapper = SQLiteConnectionWrapper(conn)
    # garantir que as tabelas existam
    _init_db(wrapper)
    return wrapper
  except Exception as e:
    print(f"Erro ao abrir/crear o banco SQLite: {e}")
    return None


if __name__ == '__main__':
  conn = conectar()
  if conn:
    print(f"Conectado ao banco SQLite em: {DB_FILE}")
    conn.close()
  else:
    print("Falha ao conectar/criar o banco SQLite.")
