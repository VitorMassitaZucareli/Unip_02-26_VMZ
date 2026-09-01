nome = input("DIGITE SEU NOME: ")
while len(nome) <= 3:
    print("NOME INVÁLIDO")
    nome = input("DIGITE SEU NOME NOVAMENTE: ")
idade = int(input("DIGITE SUA IDADE: "))
while idade < 0 or idade > 150:
    print("IDADE INVÁLIDA")
    idade = int(input("DIGITE SUA IDADE NOVAMENTE: "))
salario = float(input("DIGITE SEU SALÁRIO: "))
while salario <= 0:
    print("SALÁRIO INVÁLIDO")
    salario = float(input("DIGITE SEU SALÁRIO NOVAMENTE: "))
estado = input("ESTADO CIVIL [S/C/V/D]: ").lower()
while estado != "s" and estado != "c" and estado != "v" and estado != "d":
    print("ESTADO CIVIL INVÁLIDO")
    estado = input("ESTADO CIVIL [S/C/V/D]: ").lower()
print("TODOS OS DADOS SÃO VÁLIDOS!")
