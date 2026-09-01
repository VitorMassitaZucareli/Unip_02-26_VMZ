quant=int(input("DIGITE A QUANTIDADE DE PRODUTOS: "))
if quant >= 10:
    precoproduto=8
else:
    precoproduto=10
preco=quant*precoproduto
print(f"A COMPRA SAIRA POR: R${preco:0.2f}")