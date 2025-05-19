#-----------DICIONARIOS----------


# criar
aluno = {
    "nome": "Takase",
    "idade": 16,
    "altura": 1.87,
    "matriculado": True
}
objeto = {
    "nome": "garrafa",
    "cor": "roxo",
    "marca": "SKY FIT",
    "material": "plastico"

}

objeto2 = {
    "nome": "mouse",
    "material": "plastico",
    "marca": "VXE",
    "cor": "preto"
}

objeto3 = {
    "nome": "colar",
    "material": "couro/metal",
    "cor": "prata/preto",
    "marca": "morana"
}



# adicionar campo
aluno["peso"] = 100

#print(aluno)

# alterar campo
aluno["idade"] = 17
#print(aluno)


# deletar campo


del aluno["altura"]
#print(aluno)

# verificar
if "altura" in aluno:
    print("altura existente")
else:
    print("alutura inexistente")
# exibir

for chave, valor in aluno.items():
    print(f"{chave}: {valor}:")
    
#exibir uma lista de dicionarios
lista_objetos = [objeto, objeto2, objeto3]

    #escolhendo os campos
for objeto in lista_objetos:
    print(f"{objeto['marca']}")
    print()
    #exibindo todos
for objeto in lista_objetos:
    for chave, valor in objeto.items():
        print(f"{chave}: {valor}:")
    print()