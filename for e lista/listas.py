#etapa 1 - criar uma lista de objetos com 5 itens
objetos = ["mesa", "cadeira", "lapis", "garrafa", "relogio"]
print('lista de objetos criadas')
#etapa 2  - adicionar um outro item
objetos.append("borracha")
print(objetos)

#etapa 3 - acesse o pbjeto da posição 2
objetos[1]
quem_é = objetos[1]
print(quem_é)

#etapa 4 - remova um objeto
objetos.remove("borracha")
print(objetos)
# etapa 5 - mostrar a quantidade de objetos na lista
print(len(objetos))
#etapa 6 mostrar todos os itens
for objeto in objetos:
    print(objeto)
#etapa 7 - verifique se tem cadeira se tiver remova se não adicione
if "cadeira" in objetos:
    objetos.remove("cadeira")
    print(objetos)
else:
    objetos.append("cadeira")
    print(objetos)

#etapa 8 - ajustar a lista em ordem alfabetica e mostrar o antes e o depois
print(objetos, "antes")
objetos.sort()
print(objetos, "depois")

#etapa 9 - mostrar o primeiro e ultimo itens da lista

objetos[0]
primeiro = objetos[0]
print(primeiro)
print(objetos[len(objetos) - 1])



#etapa 10 - limpar a lista inteira

objetos.clear()
print(objetos)







