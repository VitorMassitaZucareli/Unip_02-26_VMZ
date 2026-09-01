Somanota=0
count=0
quantidade = int(input("QUANTAS NOTAS VOCÊ DESEJA INSERIR? "))
while count<quantidade:
    nota= int(input("DIGITE SUA NOTA: "))
    count=count+1
    Somanota=Somanota+nota
media=Somanota/quantidade
print(f"A MEDIA DAS NOTAS É: {media}")
