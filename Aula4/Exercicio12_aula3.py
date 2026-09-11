import random
numero_secreto = random.randint(1, 50)
tentativas = 0
palpite = int(input("DIGITE UM NÚMERO ENTRE 1 E 50: "))
while palpite != numero_secreto:
    tentativas = tentativas + 1
    if palpite < numero_secreto:
        print("O NÚMERO SECRETO É MAIOR")
    else:
        print("O NÚMERO SECRETO É MENOR")
    palpite = int(input("TENTE NOVAMENTE: "))
tentativas = tentativas + 1
print(f"VOCÊ ACERTOU EM {tentativas} TENTATIVAS!")