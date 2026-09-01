num1=float(input("DIGITE O PRIMEIRO NUMERO: "))
num2=float(input("DIGITE O SEGUNDO NUMERO: "))
operacao=input("DIGITE A OPERACAO DESEJADA: ")
if operacao == "+":
    resultado=num1+num2
    print(f"O RESULTADO DA SOMA É: {resultado:0f}")
elif operacao == "*":
    resultado=num1*num2
    print(f"O RESULTADO DA MULTIPLICAÇÃO É: {resultado:0f}")
elif operacao == "-":
    resultado=num1-num2
    print(f"O RESULTADO DA SUBTRAÇÃO É: {resultado:0f}")
elif operacao=="/":
    if num2==0:
        print("NÃO É POSSIVEL DIVIDIR POR ZERO")
    else:
        resultado=num1/num2
        print(f"O RESULTADO DA DIVISÃO É: {resultado:0f}")