mensagem = input("digite uma mensagem ")

Periodo = input("digite qual periodo estamos (manha, tarde, noite)")

Saudação = ""

if Periodo == "manha":
    Saudação = "bom dia"
    print(Saudação, "pessoal", mensagem)
elif Periodo == "tarde":
    Saudação = "Boa tarde"
    print(Saudação, "pessoal", mensagem)
elif Periodo == "noite":
    Saudação = "Boa Noite"
    print(Saudação, "pessoal", mensagem)

else:
    print("isso não é um periodo")
    pass