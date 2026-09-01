nummax=-100
num1=float(input("DIGITE O PRIMEIRO NUMERO: "))
num2=float(input("DIGITE O SEGUNDO NUMERO: "))
num3=float(input("DIGITE O TERCEIRO NUMERO: "))
if num1 >= num2 and num1 >= num3:
    nummax= num1
elif num2>=num1 and num2>= num3:
    nummax= num2
else:
    nummax= num3
print(f"O MAIOR NUMERO É: {nummax:0f}")