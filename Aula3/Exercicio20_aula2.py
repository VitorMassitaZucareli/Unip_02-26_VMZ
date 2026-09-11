valorcasa=float(input("Digite o valor da casa: "))
salario=float(input("Digite o salário do comprador: "))
quantidademeses=int(input("Digite a quantidade de meses para pagar: "))
if quantidademeses<=420:
    print("O EMPRESTIMO PODE SER REALIZADO")
prestacao=valorcasa/quantidademeses
if prestacao>salario*0.3:
    print("O VALOR DA PRESTACAO E MAIOR QUE 30% DO SALARIO,\nNAO E POSSIVEL REALIZAR O EMPRESTIMO")
elif prestacao<=salario*0.3:
    print("O VALOR DA PRESTACAO E MENOR OU IGUAL A 30% DO SALARIO,\n EMPRESTIMO APROVADO") 
     