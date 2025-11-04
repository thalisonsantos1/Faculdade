from database import conectar

#create (inserir)

def criar_clientes(nome, telefone, email):
    "Insere um novo cliente no banco de dados."
    conn = conectar() #obtém uma nova conexão
    if conn is None:
        return #Se a conexão falhou, não faz nada
    
    try:
        with conn.cursor() as cursor:
            #SQL Parametrização para evitar SQL Injection
            sql = "Insert into clientes (nome, telefone, email) values (%s, %s, %s) returning cliente_id"
            # executa o comando SQL. Passamos os valores como Tupla
            cursor.execute(sql, (nome, telefone, email))
            # pega o ID do cliente que acabou de ser inserida
            id_novocliente = cursor.fetchone()[0]
            #confirma a transação
            conn.commit()
            print (f"Cliente '{nome}' inserido com sucesso! ID: {id_novocliente}")
    except Exception as e:
        # se der erro, desfaz a transação
        conn.rollback()
        print(f"Erro ao inserir cliente: {e}")
    finally:
        conn.close()

# READ (listar/ler)

def listar_clientes():
    "Listar todos os clientes cadastradas no banco de dados."
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            #select simples para listar clientes
            cursor.execute ("SELECT cliente_id, nome, telefone, email FROM clientes order by nome")
            #pega os resultados
            clientes = cursor.fetchall()
            if not clientes:
                print ("Nenhum cliente cadastrado.")
                return
            print ("\n --- Lista de Clientes ---")
            #imprime o conteúdo de clientes

            for cliente in clientes:
                # cliente[0] é cliente_id, cliente[1] é nome, cliente[2] é telefone, cliente[3] é email
                print (f"ID: {cliente[0]} - Nome: {cliente[1]} - Telefone: {cliente[2]} - Email: {cliente[3]}")

    except Exception as e:
        print(f"Erro ao listar clientes: {e}")
    finally:
        conn.close()


# UPDATE (atualizar)

def atualizar_cliente(cliente_id, novo_nome, novo_telefone, novo_email):
    "Atualiza os dados de um cliente no banco de dados."
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            #SQL Parametrização para evitar SQL Injection        
            sql = "UPDATE clientes SET nome = %s, telefone = %s, email = %s WHERE cliente_id = %s RETURNING cliente_id"
            #a ordem dos parametros da tupla (novo_nome, novo_telefone, novo_email, cliente_id) deve bater com a ordem %s no sql
            cursor.execute(sql, (novo_nome, novo_telefone, novo_email, cliente_id))
            # cursor.rowcount diz quantas linhas foram afetadas pela atualização
        if cursor.rowcount == 0:
            print(f"Nenhum cliente encontrado com o ID {cliente_id}. Nada foi atualizado")
        else:
            #se afetou alguma linha, commita a transação
            conn.commit()
            print(f"Cliente com o ID {cliente_id} atualizado com sucesso!")
            print(f"Novos dados: Nome: '{novo_nome}', Telefone: '{novo_telefone}', Email: '{novo_email}'")
    except Exception as e:
        # se der erro, desfaz a transação
        conn.rollback()
        print(f"Erro ao atualizar cliente: {e}")
    finally:
        conn.close()

#delete (excluir)

def excluir_cliente(cliente_id):
    "Exclui um cliente do banco de dados."
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM clientes WHERE cliente_id = %s"
            cursor.execute(sql, (cliente_id,))
            if cursor.rowcount == 0:
                print (f"Nenhum cliente encontrado com o ID {cliente_id}. Nada foi excluído.")
            else:
                conn.commit()
                print (f"Cliente com o ID {cliente_id} excluido com sucesso.")
    except Exception as e:
        # se der erro, desfaz a transação
        conn.rollback()
        print(f"Erro ao excluir cliente: {e}")

        # explicação didática importante

        #print ('"Nota: Se esta ediroa estiver sendo usada por um livro na "tbl_livro", o PostgreSQL vai impedir a exclusão (erro de chave estrangeira). Mesmo que seu SQL tenha 'On delete cascade' (isso aplica se aplica a tbl_livro), nao a tbl_cliente sendo referenciada"')

    finally:
        conn.close


# ----------Menu Principal


def menu ():
    """Exibe o menu de opções para o usuário"""
    while True:
        print ("\n --- CRUD de clientes (Petshop) ---")
        print ("1 - Listar Clientes")
        print ("2 - Adicionar cliente")
        print ("3 - Atualizar cliente")
        print ("4 - Excluir cliente")
        print ("5 - Sair")

        opcao = input ("Escolha uma opção: ")

        if opcao == "1":
            listar_clientes()
        elif opcao == "2":
            #create
            nome = input ("Digite o nome do cliente: ")
            telefone = input ("Digite o telefone do cliente: ")
            email = input ("Digite o e-mail do cliente: ")
            
            if nome.strip (): #verifica se o nome não está vazio
                criar_clientes (nome, telefone, email)
            else:
                print ("O nome do cliente nao pode estar vazio. Por favor, tente novamente.")
        elif opcao == "3":
            # update
            cliente_id = input("Digite o ID do cliente a ser atualizado: ")
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            novo_email = input("Digite o novo e-mail: ")
            
            if cliente_id.isdigit() and novo_nome.strip():
                atualizar_cliente(int(cliente_id), novo_nome, novo_telefone, novo_email)
            else:
                print("ID inválido ou nome vazio. Tente novamente.")

        elif opcao == "4":
            #delete
            try:
                cliente_id = int (input ("Digite o ID do cliente que deseja excluir: "))
                #confirmação de segurança
                confirm = input (f"Tem certeza que deseja excluir o cliente {cliente_id}? (S/N): ").lower()
                if confirm == "s":
                    excluir_cliente (cliente_id)
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

    