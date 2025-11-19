def menu_principal():
    """Exibe o menu principal com opções para clientes e funcionários"""
    while True:
        print("\n" + "="*50)
        print("           SISTEMA PETSHOP")
        print("="*50)
        print("1 - Gerenciar Clientes")
        print("2 - Gerenciar Funcionários")
        print("3 - Sair do Sistema")
        print("="*50)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            from app_petshop_clientes import menu_clientes
            menu_clientes()
        elif opcao == "2":
            from app_petshop_funcionarios import menu_funcionarios
            menu_funcionarios()
        elif opcao == "3":
            print("\nObrigado por usar o Sistema Petshop! Até logo! 👋")
            break
        else:
            print("❌ Opção inválida. Por favor, escolha 1, 2 ou 3.")