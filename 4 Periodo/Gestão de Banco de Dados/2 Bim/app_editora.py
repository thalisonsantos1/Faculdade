from database import conectar

#create (inserir)

def criar_editora(nome):
    "Insere uma nova editora no banco de dados."
    conn = conectar() #obtém uma nova conexão
    if conn is None:
        return #Se a conexão falhou, não faz nada
    
    try:
        with conn.cursor() as cursor:
            #SQL Parametrização para evitar SQL Injection
            sql = "Insert into tbl_editora (nomeeditora)" "values (%s) returning ideditora"
            # executa o comando SQL. Passamos os valores como Tupla
            cursor.execute(sql, (nome,))
            # pega o ID da editora que acabou de ser inserida
            id_nova_editora = cursor.fetchone()[0]
            #confirma a transação
            conn.commit()
            print (f"Editora '{nome}' inserida com sucesso! ID: {id_nova_editora}")
    except Exception as e:
        # se der erro, desfaz a transação
        conn.rollback()
        print(f"Erro ao inserir editora: {e}")
    finally:
        conn.close()

# READ (listar/ler)

def listar_editoras():
    "Listar todas as editoras cadastradas no banco de dados."
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            #select simples para listar editoras
            cursor.execute ("SELECT ideditora, nomeeditora FROM tbl_editora order by nomeeditora")
            #pega os resultados
            editoras = cursor.fetchall()
            if not editoras:
                print ("Nenhuma editora cadastrada.")
                return
            print ("\n --- Lista de Editoras ---")
            #ikmprime o conteúdo de editoras

            for editora in editoras:
                # editora [0] é ideditora, editora [1] é nomeeditora
                print (f"ID: {editora[0]} - Nome: {editora[1]}")

    except Exception as e:
        print(f"Erro ao listar editoras: {e}")
    finally:
        conn.close()


# UPDATE (atualizar)

def atualizar_editora (id_editora, novo_nome):
    "Atualiza o nome de uma editora no banco de dados."
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            #SQL Parametrização para evitar SQL Injection
        sql = "UPDATE tbl_editora SET nomeeditora = %s WHERE ideditora = %s where ideditora = %s"
        #a ordem dos parametros da tupla (novo_nome, id_editora) deve bater com a ordem %s no sql
        cursor.execute(sql, (novo_nome, id_editora, id_editora))
        # cursor.rowcount diz quantas linhas foram afetadas pela atualização
        if cursor.rowcount == 0:
            print (f"Nenhuma editora encontrada com o ID {id_editora}. Nada foi atualizado")
        else:
            #se afetou alguma linha, commita a transação
            conn.commit()
            print (f"Editora com o ID {id_editora} atualizada com sucesso para '{novo_nome}'")
    except Exception as e:
        # se der erro, desfaz a transação
        conn.rollback()
        print(f"Erro ao atualizar editora: {e}")
    finally:
        conn.close

#delete (excluir)

def excluir_editora(id_editora):
    "Exclui uma editora do banco de dados."
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM tbl_editora WHERE ideditora = %s"
            cursor.execute(sql, (id_editora,))
            if cursor.rowcount == 0:
                print (f"Nenhuma editora encontrada com o ID {id_editora}. Nada foi excluído.")
            else:
                conn.commit()
                print (f"Editora com o ID {id_editora} excluida com sucesso.")
    except Exception as e:
        # se der erro, desfaz a transação
        conn.rollback()
        print(f"Erro ao excluir editora: {e}")

        # explicação didática importante

        print ("Nota: Se esta ediroa estiver sendo usada por um livro na "tbl_livro", o PostgreSQL vai impedir a exclusão (erro de chave estrangeira). Mesmo que seu SQL tenha 'On delete cascade' (isso aplica se aplica a tbl_livro), nao a tbl_editora sendo referenciada")

    finally:
        conn.close