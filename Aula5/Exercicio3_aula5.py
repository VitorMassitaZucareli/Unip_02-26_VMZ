def validar_formato_cpf():
    cpf = input("Digite um CPF (somente números): ")
    while len(cpf) != 11 or not cpf.isdigit() or len(set(cpf)) == 1:
        print("CPF inválido. Certifique-se de digitar apenas números e que o CPF tenha 11 dígitos.")
        cpf = input("Digite um CPF somente números: ")
    print("CPF válido!")
validar_formato_cpf()
    