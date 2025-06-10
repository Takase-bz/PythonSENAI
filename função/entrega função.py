peso =  int(input("diga o peso"))
distancia  = int(input("diga a distancia em km"))
taxa_fixa = int(input("diga o preço da taxa fixa"))
def calcular_valor(peso, distancia):
    valor_frete = (peso * 0.5) + (distancia * 0.1) + taxa_fixa
    #return valor_frete
    print("o valor sera de ", valor_frete)


calcular_valor(peso, distancia)