from database import conectar

#create (inserir)

def criar_editora(nome):
    "Insere uma nova editora no banco de dados."
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO editora (nome) VALUES (%s)", (nome,))
    conn.commit()
    cursor.close()
    conn.close()