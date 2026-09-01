#0 a 12 anos: Criança ● 13 a 17 anos: Adolescente ● 18 a 59 anos: Adulto ● 60 anos ou mais: Idoso 
idade=int(input("DIGITE SUA IDADE: "))
if idade <0:
    print("DIGITE SUA IDADE REAL")
elif 0<idade<=12:
    print("CRIANÇA")
elif 13<idade<=17:
    print("ADOLESCENTE")
elif 18<idade<=59:
    print("ADULTO")
else:
    print("IDOSO")