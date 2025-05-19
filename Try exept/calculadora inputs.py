
def soma_numeros(x1,x2):
    soma = x1 + x2
    return soma

def subtração_numeros(x1,x2):
    subtração = x1-x2
    return subtração
   
def multiplicação_numeros(x1,x2):
    multiplicação = x1*x2
    return multiplicação

def divisão_numeros(x1,x2):
    divisão = x1/x2
    return divisão

def total12promax(x1,x2):
    soma = x1 + x2
    subtração = x1-x2
    multiplicação = x1*x2
    divisão = x1/x2
    calculo1 = soma,subtração,multiplicação,divisão
    return calculo1
   
def exibir_n():
  
    print("Defina dois numeros para efetuar contas basicas")
    print("")
    print("[1] Soma")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Todos")
    print("")
    
    
    while True:    
        try:
            x1 = int(input("1ºNumero: "))
            print("")
            break
          #  except IndexError:
           #     print("erro, escreva um numero")
        except ValueError:
            print("ERRO: escreva um numero existente da tabela")
            

    while True:
        try:       
            x2 = int(input("2ºNumero: "))
            print("")
            break
            #xcept IndexError:
              #  print("erro, escreva um numero")
        except ValueError:
            print("ERRO: escreva um numero existente da tabela")
           

    while True:
        try:        
            num1 = int(input("Numero de [1-5]: "))
            print("")
            #break
          #  except IndexError:
          #      print("erro, escreva um numero")
        except ValueError:
            print("ERRO: escreva um numero existente da tabela")
            



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
            print("Erro")
            print("")

exibir_n()
