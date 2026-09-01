salario=float(input("Digite o salário do funcionário: "))
if salario <=2000:
    aumento=1.15
    salariofinal=salario*aumento
    print(f"O salário final do funcionário é: R${salariofinal:.2f}")
elif salario >2000 and salario <=5000:
    aumento=1.1
    salariofinal=salario*aumento
    print(f"O salário final do funcionário é: R${salariofinal:.2f}")
else:
    aumento=1.05
    salariofinal=salario*aumento
    print(f"O salário final do funcionário é: R${salariofinal:.2f}")