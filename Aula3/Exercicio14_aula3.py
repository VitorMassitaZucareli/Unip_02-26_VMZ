numero = 1
while numero <= 500:
    soma = 0
    divisor = 1
    while divisor < numero:
        if numero % divisor == 0:
            soma = soma + divisor
        divisor = divisor + 1
    if soma == numero:
        print(numero)
    numero = numero + 1