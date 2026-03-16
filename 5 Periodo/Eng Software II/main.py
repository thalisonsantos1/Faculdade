from logger import Logger

def processar_dados():
    logger = Logger()
    logger.info("Processando dados...")
    logger.warning("Tempo de processamento alto")

def salvar_resultados():
    logger = Logger()
    logger.info("Salvando resultados no disco")

if __name__ == "__main__":
    logger1 = Logger()
    logger1.info("Aplicação iniciada")

    processar_dados()

    logger1.warning("Memória baixa")

    salvar_resultados()

    logger1.error("Falha na conexão com o banco de dados")

    logger2 = Logger()

    print("\n--- Verificando se é a mesma instância ---")
    print(f"ID logger1: {id(logger1)}")
    print(f"ID logger2: {id(logger2)}")
    print(f"logger1 e logger2 são o mesmo objeto? {logger1 is logger2}")