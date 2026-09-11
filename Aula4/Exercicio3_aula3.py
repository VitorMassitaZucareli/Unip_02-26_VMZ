numero1=int(input("DIGITE UM NUMERO: "))
numero2=int(input("DIGITE UM NUMERO: "))
print("VAMOS VER OS NUMEROS PARES NO ITNERVALO DESSES 2 NUMEROS")
if numero1>numero2:
    while numero1 !=numero2:
        if numero1 % 2 == 0:
            print(numero1)
        numero1 = numero1 - 1
else:
    while numero2 !=numero1:
            if numero2 % 2 == 0:
                print(numero2)
            numero2 = numero2 - 1