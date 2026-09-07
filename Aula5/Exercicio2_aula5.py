def analisar_numeros():
    quantnumero=0
    somanumero=0
    nummax=-10000
    nummin=10000
    numero=int(input("Digite um número inteiro: "))
    while numero != 0:
        quantnumero+=1
        somanumero+=numero
        if numero>nummax:
            nummax=numero
        if numero<nummin:
            nummin=numero
        numero=int(input("Digite um número inteiro: "))
    print("Quantidade de números digitados:", quantnumero)
    print("Soma dos números digitados:", somanumero)
    print("Média dos números digitados:", somanumero/quantnumero)
    print("Número máximo:", nummax)
    print("Número mínimo:", nummin)
analisar_numeros()