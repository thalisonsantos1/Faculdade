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
            sql = "UPDATE tbl_editora SET nomeeditora = %s WHERE ideditora = %s RETURNING ideditora"
            #a ordem dos parametros da tupla (novo_nome, id_editora) deve bater com a ordem %s no sql
            cursor.execute(sql, (novo_nome, id_editora))
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

        #print ('"Nota: Se esta ediroa estiver sendo usada por um livro na "tbl_livro", o PostgreSQL vai impedir a exclusão (erro de chave estrangeira). Mesmo que seu SQL tenha 'On delete cascade' (isso aplica se aplica a tbl_livro), nao a tbl_editora sendo referenciada"')

    finally:
        conn.close


# ----------Menu Principal


def menu ():
    """Exibe o menu de opções para o usuário"""
    while True:
        print ("\n --- CRUD de Editoras (Biblioteca) ---")
        print ("1 - Litsar editoras")
        print ("2 - Adicionar editora")
        print ("3 - Atualizar editora")
        print ("4 - Excluir editora")
        print ("5 - Sair")

        opcao = input ("Escolha uma opção: ")

        if opcao == "1":
            listar_editoras()
        elif opcao == "2":
            #create
            nome = input ("Digite o nome da editora: ")
            if nome.strip (): #verifica se o nome não está vazio
                criar_editora (nome)
            else:
                print ("O nome da editora nao pode estar vazio. Por favor, tente novamente.")
        elif opcao == "3":
            #update
            try:
                id_ed = int (input ("Digite o ID da editora que deseja atualizar: "))
                novo_nome = input ("Digite o novo nome da editora: ")
                if novo_nome.strip ():
                    atualizar_editora (id_ed, novo_nome)
                else:
                    print ("O nome da editora nao pode estar vazio. Por favor, tente novamente.")
            except Exception as e:
                print ("ID inválido. Por favor, digite um número inteiro.")

        elif opcao == "4":
            #delete
            try:
                id_ed = int (input ("Digite o ID da editora que deseja excluir: "))
                #confirmação de segurança
                confirm = input (f"Tem certeza que deseja excluir a editora {id_ed}? (S/N): ").lower()
                if confirm == "s":
                    excluir_editora (id_ed)
                else:
                    print ("Exclusão cancelada.")
            except Exception as e:
                print ("ID inválido. Por favor, digite um número inteiro.")
        elif opcao == "5":
            print ("Saindo...")
            break #quebra o loop while true e encerra o programa
        else:
            print ("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__': #ponto de entrada do script
    menu()

    