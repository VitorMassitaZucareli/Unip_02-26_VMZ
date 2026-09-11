dia=int(input("Digite o dia: "))
mes=int(input("Digite o mês: "))
ano=ano = int(input("Digite um ano: "))
if mes== 1 or mes==3 or mes==5 or mes==7 or mes==9 or mes==11:
    quantidade_dias=31
elif mes==4 or mes==6 or mes==8 or mes==10 or mes==12:
    quantidade_dias=30
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    if mes==2:
        quantidade_dias=29
else:
    if mes==2:
        quantidade_dias=28
if dia>=1 and dia<=quantidade_dias:
    print("Data válida!")
else:
        print("Data inválida!") 