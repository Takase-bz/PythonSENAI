nota_1 = float(input("solicite uma nota"))

nota_2 = float(input("solicite outra nota"))
if nota_1 > 0 and nota_1 < 100 and nota_2 > 0 and nota_2 < 100:
    print("")
    nota_3 = nota_1 + nota_2

    nota_4 = nota_3 / 2

    if nota_4 < 50:
            print("")
            print(nota_4)
            print("mostre reprovado")
    elif nota_4 <= 70 and nota_4 >= 50:
        print(nota_4)
        print("mostre recuperação")
    elif nota_4 >= 70:
        print(nota_4)
        print("mostre aprovado")
else:
    print("o numero deve ser de 0 a 100")
            
