import random

print("Bem-vindo ao Jogo de Adivinhação!")

print("ADIVINHE O NUMERO DE 1 A 100!")
n_aleatorio = random.randint(1,100)

while True:

    palpite = int(input("digite o seu palpite"))

    if palpite == n_aleatorio:
        print("parabens você acertou")
        n_aleatorio = random.randint(1,100)
        print("")
        print("[1] jogar novamente")
        print("[0] sair")
        num = input("Numero de [0-1]: ")
        print("")
        if num == "0":
            print("Sair")
            break
        
    elif palpite < n_aleatorio:
        print("tente um numero maior")
    else:
        print("tente um numero menor")
        
   
    
    

    