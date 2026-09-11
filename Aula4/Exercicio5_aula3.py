nota=int(input("DIGITE SUA NOTA: "))
count=0
while count !=1:
    if nota >10 or nota<0:
        print("DIGITE UMA NOTA VALIDA")
        count = count+1
    else:
        print("NOTA VALIDA")
        