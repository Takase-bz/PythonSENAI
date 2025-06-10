distancia = int(input("diga a distancia em km"))
velocidade = int(input("diga a velocidade"))
def medir_tempo(velocidade, distancia):
    tempo = distancia / velocidade
    print(" o tempo sera de ", tempo, "horas")
    
    #return tempo
#print(tempo)
medir_tempo(velocidade, distancia)