import os
from datetime import datetime

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._log_file = "aplicacao.log"
        return cls._instance

    def _log(self, nivel, mensagem):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linha = f"[{timestamp}] {nivel}: {mensagem}"
        print(linha)
        self._salvar_em_arquivo(linha)

    def info(self, mensagem):
        self._log("INFO", mensagem)

    def warning(self, mensagem):
        self._log("WARNING", mensagem)

    def error(self, mensagem):
        self._log("ERROR", mensagem)

    def _salvar_em_arquivo(self, linha):
        try:
            with open(self._log_file, "a", encoding="utf-8") as arquivo:
                arquivo.write(linha + "\n")
        except Exception as e:
            print(f"Erro ao escrever no arquivo de log: {e}")