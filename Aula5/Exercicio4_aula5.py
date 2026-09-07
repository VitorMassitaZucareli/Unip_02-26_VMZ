def tabuada_personalizada():
    numero = int(input("Digite o número da tabuada: "))
    inicio = int(input("Digite o início da tabuada: "))
    fim = int(input("Digite o fim da tabuada: "))
    if inicio <= fim:
        while inicio <= fim:
            print(numero, "x", inicio, "=", numero * inicio)
            inicio = inicio + 1
    else:
        print("Erro: o valor inicial deve ser menor ou igual ao valor final.")

tabuada_personalizada()