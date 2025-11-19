from database import conectar

# CREATE (inserir)
def criar_funcionario(nome, cargo, salario):
    """Insere um novo funcionário no banco de dados."""
    conn = conectar()
    if conn is None:
        return
    
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO funcionarios (nome, cargo, salario) VALUES (%s, %s, %s) RETURNING funcionario_id"
            cursor.execute(sql, (nome, cargo, salario))
            id_novo_funcionario = cursor.fetchone()[0]
            conn.commit()
            print(f"✅ Funcionário '{nome}' inserido com sucesso! ID: {id_novo_funcionario}")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao inserir funcionário: {e}")
    finally:
        conn.close()

# READ (listar/ler)
def listar_funcionarios():
    """Lista todos os funcionários cadastrados no banco de dados."""
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT funcionario_id, nome, cargo, salario FROM funcionarios ORDER BY nome")
            funcionarios = cursor.fetchall()
            if not funcionarios:
                print("📝 Nenhum funcionário cadastrado.")
                return
            print("\n" + "="*80)
            print("                       LISTA DE FUNCIONÁRIOS")
            print("="*80)
            for funcionario in funcionarios:
                print(f"ID: {funcionario[0]} | Nome: {funcionario[1]:<20} | Cargo: {funcionario[2]:<15} | Salário: R$ {funcionario[3]:.2f}")
            print("="*80)
    except Exception as e:
        print(f"❌ Erro ao listar funcionários: {e}")
    finally:
        conn.close()

# UPDATE (atualizar)
def atualizar_funcionario(funcionario_id, novo_nome, novo_cargo, novo_salario):
    """Atualiza os dados de um funcionário no banco de dados."""
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            sql = "UPDATE funcionarios SET nome = %s, cargo = %s, salario = %s WHERE funcionario_id = %s"
            cursor.execute(sql, (novo_nome, novo_cargo, novo_salario, funcionario_id))
            if cursor.rowcount == 0:
                print(f"❌ Nenhum funcionário encontrado com o ID {funcionario_id}.")
            else:
                conn.commit()
                print(f"✅ Funcionário ID {funcionario_id} atualizado com sucesso!")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao atualizar funcionário: {e}")
    finally:
        conn.close()

# DELETE (excluir)
def excluir_funcionario(funcionario_id):
    """Exclui um funcionário do banco de dados."""
    conn = conectar()
    if conn is None:
        return
    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM funcionarios WHERE funcionario_id = %s"
            cursor.execute(sql, (funcionario_id,))
            if cursor.rowcount == 0:
                print(f"❌ Nenhum funcionário encontrado com o ID {funcionario_id}.")
            else:
                conn.commit()
                print(f"✅ Funcionário ID {funcionario_id} excluído com sucesso.")
    except Exception as e:
        conn.rollback()
        print(f"❌ Erro ao excluir funcionário: {e}")
    finally:
        conn.close()

# Menu Funcionários
def menu_funcionarios():
    """Exibe o menu de opções para gerenciamento de funcionários"""
    while True:
        print("\n" + "="*50)
        print("        GERENCIAMENTO DE FUNCIONÁRIOS")
        print("="*50)
        print("1 - Listar Funcionários")
        print("2 - Adicionar Funcionário")
        print("3 - Atualizar Funcionário")
        print("4 - Excluir Funcionário")
        print("5 - Voltar ao Menu Principal")
        print("="*50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_funcionarios()
        elif opcao == "2":
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            try:
                salario = float(input("Digite o salário do funcionário: "))
                if nome.strip():
                    criar_funcionario(nome, cargo, salario)
                else:
                    print("❌ O nome do funcionário não pode estar vazio.")
            except ValueError:
                print("❌ Salário inválido. Digite um valor numérico.")
        elif opcao == "3":
            funcionario_id = input("Digite o ID do funcionário a ser atualizado: ")
            novo_nome = input("Digite o novo nome: ")
            novo_cargo = input("Digite o novo cargo: ")
            try:
                novo_salario = float(input("Digite o novo salário: "))
                if funcionario_id.isdigit() and novo_nome.strip():
                    atualizar_funcionario(int(funcionario_id), novo_nome, novo_cargo, novo_salario)
                else:
                    print("❌ ID inválido ou nome vazio.")
            except ValueError:
                print("❌ Salário inválido. Digite um valor numérico.")
        elif opcao == "4":
            try:
                funcionario_id = int(input("Digite o ID do funcionário que deseja excluir: "))
                confirm = input(f"Tem certeza que deseja excluir o funcionário {funcionario_id}? (S/N): ").lower()
                if confirm == "s":
                    excluir_funcionario(funcionario_id)
                else:
                    print("⚡ Exclusão cancelada.")
            except ValueError:
                print("❌ ID inválido. Digite um número inteiro.")
        elif opcao == "5":
            print("↩️ Voltando ao Menu Principal...")
            break
        else:
            print("❌ Opção inválida. Escolha de 1 a 5.")