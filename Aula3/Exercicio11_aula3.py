palavra=str(input("DIGITE UMA PALAVRA: "))
texto=palavra
quantvogal=0
quantconsoante=0
if texto[1] == "a" or texto[1] == "E" or texto[1] == "I" or texto[1] == "O" or texto[1] == "U" or texto[1] == "e" or texto[1] == "i" or texto[1] == "o" or texto[1] == "u":
    quantvogal=quantvogal+1
else:
    quantconsoante=quantconsoante+1
print(f"A QUANTIDADE DE VOGAIS É: {quantvogal}")
print(f"A QUANTIDADE DE CONSOANTES É: {quantconsoante}")