print("solicite o ano de nasciento ")
idade = float(input("digite o ano atual"))

idade2 = float(input("solicite o ano de nascimento"))

calculo1 = idade - idade2

if calculo1 <= 17:
    print(round(calculo1))
    print("menor de idade")
elif calculo1 >= 18:
    print(round(calculo1))
    print("maior de idade")
else:
    print("erro")