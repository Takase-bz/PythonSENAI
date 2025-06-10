estação  = input("diga a estação")
temperatura = float(input("cite a temperatura "))
humidade = float(input("digite a humidade "))

def medir_temperatura(estação, temperatura, humidade):
    if estação == "inverno":
        if  temperatura >= 20 and temperatura <= 22 and humidade >= 40 and humidade <= 55  :
            print("temperatura e humidade  boa ")
        else:
            print("não adequada")
    elif estação ==  "verão":
        if temperatura >= 23 and temperatura <= 26 and humidade >= 40 and humidade <= 65:
            print("adequado")
        else:
            print("não adequado")
    else:
        print("erro")
            
            
print(medir_temperatura(estação, temperatura, humidade))
        