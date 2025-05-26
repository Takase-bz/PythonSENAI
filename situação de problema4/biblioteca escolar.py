from Tryexept import inputs
lista_livros = []
    
while True:
    print("Biblioteca escolar ")
    print("[1] - Adicionar Livro")
    print("[2] - exibir todos os livros ")
    print("[3] - exibir a quantidade de livros ")
    print("[4] - titulos dos livros cadastrados ")
    print("[5] - mostrar os livros do autor especifico")
    print("[6] - mostrar os livros de um determinado tema ")
    print("[7] - editar dados de livros ")
    num = input("digite um numero de 1 ao 7 = ")
    if num == "1":
        
        livro = { "titulo": inputs.input_str('digite o nome do livro'),
        "autor": inputs.input_str('digite o autor'),
        "ISBN": inputs.input_int("digite o numero ISBN"),
        "categoria": inputs.input_str('digite a categoria'),
        "ano publicado": inputs.input_int("digite o numero"),
                  }
        if livro in lista_livros:
            print("este nome já está na lista ")
        else:
            lista_livros.append(livro)
            print("nome adicionado ")
            
    elif num == "2":
         lista_livros.sort()
         print("lista dos livros  ")
         for livro in lista_livros:
                for chave, valor in livro.items():
                    print(f"{chave}: {valor}:")
                   
                    
        
    elif num == "3":
        print("a quantidade de livros é ", len(lista_livros))
    elif num == "4":
        for livro in lista_livros:
            print(f"{livro['titulo']}")
            print("")
    elif num == "5":
        autor_escolhido =  inputs.input_str("nome do autor")
        for livro in lista_livros:
            if autor_escolhido == livro['autor']:
                for chave, valor in livro.items():
                    print(f"{chave}: {valor}:")
        print("")
    elif num == "6":
        categoria_escolhida = inputs.input_str("escolha a categoria")
        for livro in lista_livros:
            if categoria_escolhida == livro['categoria']:
                for chave, valor in livro.items():
                    print(f"{chave}: {valor}:")
                
    
        
    elif num == "7":
        isbn_editar = inputs.input_int("digite o isbn do livro")
        for livro in lista_livros:
            if livro['ISBN'] == isbn_editar:
                print("livro encontrado, faça as alterações")
                livro['titulo'] = inputs.input_str("digite o novo titulo")
                livro['autor'] = inputs.input_str("digite o nome do autor")
                livro['ano'] = inputs.input_int("digite o ano do nascimento")
                livro['categoria'] = inputs.input_str("digite a categoria")
                
                print("alteração feita")
                break