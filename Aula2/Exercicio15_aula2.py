#Abaixo de 18.5: Abaixo do peso ● 18.5 a 24.9: Peso normal ● 25.0 a 29.9: Sobrepeso ● 30.0 ou mais: Obesidade
peso=float(input("DIGITE SEU PESO: "))
altura=float(input("DIGITE SUA ALTURA EM CENTIMETROS: "))
imc=peso/(altura/100)**2
if imc<18.5:
    print("VOCE ESTA ABAIXO DO PESO")
elif 18.5<=imc<=24.9:
    print("VOCE ESTA COM PESO NORMAL")
elif 25<imc<29.9:
    print("VOCE ESTA COM SOBREPESO")
else:
    print("VOCE ESTA COM OBESIDADE")