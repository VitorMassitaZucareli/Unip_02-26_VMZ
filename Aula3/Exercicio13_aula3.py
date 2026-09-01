maiores18 = 0
homens = 0
mulheres20 = 0
continuar = "S"
while continuar == "S":
    idade = int(input("DIGITE A IDADE: "))
    sexo = input("DIGITE O SEXO [M/F]: ").upper()
    if idade > 18:
        maiores18 = maiores18 + 1
    if sexo == "M":
        homens = homens + 1
    if sexo == "F" and idade < 20:
        mulheres20 = mulheres20 + 1
    continuar = input("DESEJA CONTINUAR? [S/N]: ").upper()
print(f"PESSOAS COM MAIS DE 18 ANOS: {maiores18}")
print(f"HOMENS CADASTRADOS: {homens}")
print(f"MULHERES COM MENOS DE 20 ANOS: {mulheres20}")