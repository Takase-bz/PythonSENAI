numero = float(input("cite um numero "))
def verificar_positivo(numero):
    if numero >= 1:
        #print("numero negativo")
        return True 
        #print(verificar_positivo())
        #print(numero)
    elif numero <= -1:
        print()
        return False
        #print("numero positivo")
    else:
        print("erro")
          
print(verificar_positivo(numero))
if numero <= -1:
    print("numero negativo")
elif numero >= 1:
    print("numero positivo")
 
        
