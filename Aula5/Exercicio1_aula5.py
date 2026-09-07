def validar_senha():
    senha = input("Digite uma senha: ")
    while (len(senha) < 8
        or not any(char.isnumeric() for char in senha)
        or not any(char.isupper() for char in senha)):
        if len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
        if not any(char.isnumeric() for char in senha):
            print("A senha deve conter pelo menos um número.")
        if not any(char.isupper() for char in senha):
            print("A senha deve conter pelo menos uma letra maiúscula.")
        senha = input("Digite uma senha: ")
    print("Senha válida!")
validar_senha()