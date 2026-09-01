#9.0 a 10: A ● 7.0 a 8.9: B ● 5.0 a 6.9: C ● Menor que 5.0: D 
nota=float(input("DIGITE SUA NOTA: "))
if nota>11 or nota<0:
    print("DIGITE UMA NOTA DE 1 A 10")
elif 9<nota<=10:
    print("SUA NOTA É: A")
elif 7<nota<8.9:
    print("SUA NOTA É: B")
elif 5<nota<6.9:
    print("SUA NOTA É: C")
else:
    print("SUA NOTA É: D")
