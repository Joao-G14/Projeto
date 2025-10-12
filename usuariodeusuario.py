
print("=== SISTEMA DE CADASTRO DE USUÁRIO ===")


arquivo = "usuarios.txt"


usuarios = []
try:
    with open(arquivo, "r") as f:
        for linha in f:
            nome, senha = linha.strip().split(";")
            usuarios.append([nome, senha])
except FileNotFoundError:
    pass 


while True:
    print("\nMenu:")
    print("1 - Cadastrar novo usuário")
    print("2 - Mostrar usuários cadastrados")
    print("3 - Fazer login")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome de usuário: ")
        senha = input("Digite a senha: ")

        
        existe = False
        for u in usuarios:
            if u[0] == nome:
                existe = True
                break

        if existe:
            print("⚠️ Usuário já existe, tente outro nome!")
        else:
            usuarios.append([nome, senha])
            with open(arquivo, "a") as f:
                f.write(f"{nome};{senha}\n")
            print("✅ Usuário cadastrado com sucesso!")

    elif opcao == "2":
        if len(usuarios) == 0:
            print("Nenhum usuário cadastrado ainda.")
        else:
            print("\n--- Lista de Usuários ---")
            for u in usuarios:
                print("👤", u[0])

    elif opcao == "3":
        nome = input("Usuário: ")
        senha = input("Senha: ")

        logado = False
        for u in usuarios:
            if u[0] == nome and u[1] == senha:
                logado = True
                break

        if logado:
            print("✅ Login realizado com sucesso! Bem-vindo,", nome)
        else:
            print("❌ Usuário ou senha incorretos.")

    elif opcao == "4":
        print("Encerrando o programa... Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
