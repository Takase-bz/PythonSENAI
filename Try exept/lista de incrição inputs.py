import inputs

lista_nomes = []


while True :
    print("menu do gerenciamento de inscrições ")
    print("[1] - cadastrar nome ")
    print("[2] - exibir o total de inscritos ")
    print("[3] - exibir a lista de nomes em ordem alfabética ")
    print("[4] - permitir a consulta de um nome ")
    print("[5] - sair ")

    escolha = inputs.input_int("escolha uma opção")

    if escolha == 1:
        nome = inputs.input_str("digite seu nome")
        if nome in lista_nomes:
            print("este nome já está na lista ")
        else:
            lista_nomes.append(nome)
            print("nome adicionado ")
    elif escolha == 2:
        print("a quantidade de inscritos é ", len(lista_nomes))

    elif escolha == 3:
        lista_nomes.sort()
        print("lista de alunos inscritos ")
        for nome in lista_nomes:
            print(nome)

    if escolha == 4:
        nome_consulta = inputs.input_str("digite o nome que você quer verificar: ")
        if nome_consulta in lista_nomes:
            opção = inputs.input_str("nome encontrado deseja remove-lo")
            if opção == "s":
                lista_nomes.remove(nome_consulta)
                print("nome excluido com sucesso ")
        else:
            opção2 = inputs.input_str("Nome não encontrado.Deseja adicioná-lo? (s/n)")
            if opção2 == "s":
                lista_nomes.append(nome_consulta)
                print("nome adicionado com sucesso ")

    elif escolha == 5:
        print("saindo... ")
        break