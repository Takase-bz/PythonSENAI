grana = 0
quant = 0
while True:
    print("selecione o menu desejado")
    print("")
    print("[1] Adicionar o valor da despesa")
    print("[2] mostrar quantidade e valor total das despesas")
    print("[0] sair")
    num = input("solicite um numero de [0-2]")
    
    if num == "1":
        adicionar_gasto = int(input("valor gasto"))
        grana = grana + adicionar_gasto
        quant += 1
        print(adicionar_gasto)
    elif num == "2":
        print("o gasto total é", grana)
        print("sua quantidade de contas é", quant)
    elif num == "0":
        print("sair")
        
        break 