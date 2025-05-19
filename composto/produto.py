# 1 exiba o novo preço do poroduto e quanto diminuiu
# 2 nome do produto e o o preço dele
# 3 faça o preço vezes 5
#faça o resultado por 100
#exiba o resultado


input("digite o seu produto")

produto = int(input("digite o preço"))
calculo = produto * 5
preço_rebaixado = calculo / 100
preço_novo = produto - preço_rebaixado
print("o preço com o desconto é de", preço_novo)
print(" o desconto foi de", preço_rebaixado)

