

def medir_imc2(peso, altura):
  
    imc1 = altura * altura
    imc = peso / imc1
    return imc


def medir_imc(imc):

    
    if imc <= 18.5:
        print(round(imc, 3),"= Baixo peso")
    elif imc <= 24.9:
        print(round(imc, 3),"Peso Normal")
    elif imc <= 29.9:
        print(round(imc, 3),"Sobrepeso")
    elif imc <= 34.9:
        print(round(imc, 3),"Grau 1 de Obesidade")
    elif imc <= 39.9:
        print(round(imc, 3),"Grau 2 de Obesidade")
    elif imc >= 40:
        print(round(imc, 3),"Grau 3 de Obesidade")
        
peso = float(input("digite seu peso"))
altura = float(input("digite a sua altura"))

resultado = medir_imc2(peso, altura)


medir_imc(resultado)





