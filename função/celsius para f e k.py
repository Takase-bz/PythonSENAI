print("Defina o valor dos Celsius para achar o Kelvin e Fahrenheit")

def calcular_fah(celsius):
    calculo1 = celsius * 1.8
    calculo2 = calculo1 + 32
    calculo3 = celsius + 273
    print("Valor do Kelvin: ",round(calculo3),"K",sep='')
    print("")
    print("Valor do Fahrenheit: ",round(calculo2),"ºF",sep='')

def exibir_fah():
    print("")
    celsius = int(input("Defina o valor de Celsius: "))
    print("")
    calcular_fah(celsius)
   
exibir_fah()