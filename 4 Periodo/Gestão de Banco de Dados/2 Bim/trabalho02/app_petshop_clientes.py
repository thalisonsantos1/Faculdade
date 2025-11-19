from database import conectar

# CREATE (inserir)
def criar_cliente(nome, telefone, email):
    """Insere um novo cliente no banco de dados."""
    conn = conectar()
    if conn is None:
        return
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s) RETURNING cliente_id"
            cursor.execute(sql, (nome, telefone, email))
            id_novo_cliente = cursor.fetchone()[0]
            conn.commit()
            print(f"✅ Cliente '{nome}' inserido com sucesso! ID: {id_novo_cliente}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao inserir cliente: {e}")
    finally:
        conn.close()

# READ (listar/ler)
def listar_clientes():
    """Lista todos os clientes cadastrados no banco de dados."""
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT cliente_id, nome, telefone, email FROM clientes ORDER BY nome")
            clientes = cursor.fetchall()
            if not clientes:
                print("📝 Nenhum cliente cadastrado.")
                return
            print("\n" + "="*80)
            print("                          LISTA DE CLIENTES")
            print("="*80)
            for cliente in clientes:
                print(f"ID: {cliente[0]} | Nome: {cliente[1]:<20} | Telefone: {cliente[2]:<15} | Email: {cliente[3]}")
            print("="*80)
    except Exception as e:
        print(f"❌ Erro ao listar clientes: {e}")
    finally:
        conn.close()

# UPDATE (atualizar)
def atualizar_cliente(cliente_id, novo_nome, novo_telefone, novo_email):
    """Atualiza os dados de um cliente no banco de dados."""
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE clientes SET nome = %s, telefone = %s, email = %s WHERE cliente_id = %s"
            cursor.execute(sql, (novo_nome, novo_telefone, novo_email, cliente_id))
            if cursor.rowcount == 0:
                print(f"❌ Nenhum cliente encontrado com o ID {cliente_id}.")
            else:
                conn.commit()
                print(f"✅ Cliente ID {cliente_id} atualizado com sucesso!")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao atualizar cliente: {e}")
    finally:
        conn.close()

# DELETE (excluir)
def excluir_cliente(cliente_id):
    """Exclui um cliente do banco de dados."""
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM clientes WHERE cliente_id = %s"
            cursor.execute(sql, (cliente_id,))
            if cursor.rowcount == 0:
                print(f"❌ Nenhum cliente encontrado com o ID {cliente_id}.")
            else:
                conn.commit()
                print(f"✅ Cliente ID {cliente_id} excluído com sucesso.")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao excluir cliente: {e}")
    finally:
        conn.close()

# Menu Clientes
def menu_clientes():
    """Exibe o menu de opções para gerenciamento de clientes"""
    while True:
        print("\n" + "="*50)
        print("          GERENCIAMENTO DE CLIENTES")
        print("="*50)
        print("1 - Listar Clientes")
        print("2 - Adicionar Cliente")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Voltar ao Menu Principal")
        print("="*50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_clientes()
        elif opcao == "2":
            nome = input("Digite o nome do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            email = input("Digite o e-mail do cliente: ")
            
            if nome.strip():
                criar_cliente(nome, telefone, email)
            else:
                print("❌ O nome do cliente não pode estar vazio.")
        elif opcao == "3":
            cliente_id = input("Digite o ID do cliente a ser atualizado: ")
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo telefone: ")
            novo_email = input("Digite o novo e-mail: ")
            
            if cliente_id.isdigit() and novo_nome.strip():
                atualizar_cliente(int(cliente_id), novo_nome, novo_telefone, novo_email)
            else:
                print("❌ ID inválido ou nome vazio.")
        elif opcao == "4":
            try:
                cliente_id = int(input("Digite o ID do cliente que deseja excluir: "))
                confirm = input(f"Tem certeza que deseja excluir o cliente {cliente_id}? (S/N): ").lower()
                if confirm == "s":
                    excluir_cliente(cliente_id)
                else:
                    print("⚡ Exclusão cancelada.")
            except ValueError:
                print("❌ ID inválido. Digite um número inteiro.")
        elif opcao == "5":
            print("↩️ Voltando ao Menu Principal...")
            break
        else:
            print("❌ Opção inválida. Escolha de 1 a 5.")