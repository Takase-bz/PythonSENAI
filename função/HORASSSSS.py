from datetime import datetime

def mensagem_automatica(nome):
    hora_atual = datetime.now().hour

    if hora_atual > 0 and hora_atual < 5:
        print("boa madrugada", nome, "agora são", hora_atual)


    elif hora_atual > 5 and hora_atual < 12:
        print("bom dia", nome, "agora são", hora_atual)


    elif hora_atual > 12 and hora_atual < 19:
        print("boa tarde", nome, "agora são", hora_atual)

    elif hora_atual > 19 and hora_atual < 23:
        print("boa noite", nome, "agora são", hora_atual)
        
nome = input("nome do usuario")

mensagem_automatica(nome)
    
    