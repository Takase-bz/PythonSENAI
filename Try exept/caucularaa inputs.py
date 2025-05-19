import inputs
#3.1
def soma_numeros(x1,x2):
    xs = x1 + x2
    return xs

def subtração_numeros(x1,x2):
    xs1 = x1-x2
    return xs1
   
def multiplicação_numeros(x1,x2):
    xm = x1*x2
    return xm

def divisão_numeros(x1,x2):
    xd = x1/x2
    return xd

def total12promax(x1,x2):
    xs = x1 + x2
    xs1 = x1-x2
    xm = x1*x2
    xd = x1/x2
    calc1 = xs,xs1,xm,xd
    return calc1
   
def exibir_n():
    while True:
        print("Defina dois numeros para efetuar contas basicas")
        print("")
        print("[1] Soma")
        print("[2] Subtração")
        print("[3] Multiplicação")
        print("[4] Divisão")
        print("[5] Todos")
        print("")
        num1 = inputs.input_int("Escolha: ")
        print("")
        x1 = inputs.input_float("1º Numero: ",2)
        print("")
        x2 = inputs.input_float("2º Numero: ",2)
        print("")
        print("")
        if num1 == 1:
            print("Soma:",soma_numeros(x1,x2))
            print("")
        elif num1 == 2:
            print("Subtração:",subtração_numeros(x1,x2))
            print("")
        elif num1 == 3:
            print("Multiplicação:",multiplicação_numeros(x1,x2))
            print("")
        elif num1 == 4:
            print("Divisão:",divisão_numeros(x1,x2))
            print("")
        elif num1 == 5:
            print("Total:",total12promax(x1,x2))
            print("")
        else:
            print("Numero não programado Porfavor selecionar numero da tabela:")
            print("")
exibir_n()


