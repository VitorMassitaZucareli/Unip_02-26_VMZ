horas=float(input("Digite o número de horas que voce ficou no estacionamento: "))
if horas<=2:
    preco=horas*5
    print(f"O valor a ser pago é: R${preco:.2f}")
elif horas>=3 and horas<=4:
    preco=5*2+(horas-2)*4
    print(f"O valor a ser pago é: R${preco:.2f}")
elif horas >=5:
    preco=(5*2)+(2*4)+((horas-4)*3)
    print(f"O valor a ser pago é: R${preco:.2f}")
    