nota_1 = float(input("solicite uma nota"))

nota_2 = float(input("solicite outra nota"))

nota_3 = nota_1 + nota_2

nota_4 = nota_3 / 2

if nota_4 <= 70:
    print(nota_4)
    print("mostre reprovado")
elif nota_4 >= 70:
    print(nota_4)
    print("mostrar aprovado")
else:
    pass
