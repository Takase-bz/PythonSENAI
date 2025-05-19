idade_1 = int(input("digite a sua data de nascimento"))
idade_2 = int(input("digite o ano atual"))

idade_3 = idade_2 - idade_1

if idade_3 >= 60 and idade_3 <= 116:
    print("idoso")
elif idade_3 >= 18 and idade_3 <= 59:
    print("adulto")
elif idade_3 >= 11 and idade_3 <= 17:
    print("adolescente")
elif idade_3 <= 10:
    print("criança")
else:
    print("erro")
