numero=int(input("DIGITE UM NUMERO E VAMOS CALCULAR SEU FATORIAL: "))
fatorial=1
while numero > 0:
    fatorial=fatorial*numero
    numero=numero-1
print(f"O FATORIAL É: {fatorial}")
