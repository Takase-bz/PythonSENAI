import inputs
alunos = []
def exibir_todos(alunos):
    for i in alunos:
        
            print(f"NOME - {i['nome']}")
            print(f"MEDIA - {i['media']} ")
            print(f"SITUAÇÃO - {i['situação']}")
        
def calcular_media(nota1, nota2, nota3):
    calc1 = nota1 + nota2 + nota3
    calc2 = calc1 / 3
    return calc2
def verificar_situacao(media):
    if media >= 7:
        n1 = "aprovado"
        return n1
    elif media >= 5 and media <= 6.9:
        n1 = "recuperação"
        return n1
    elif media <= 4.9:
        n1 = "reprovado"
        round (media, 1)
        return n1
def cadastrar_aluno():
    
    aluno1 = {
    "nome": inputs.input_str("nome do aluno"),
    "nota_1": inputs.input_int("nota do aluno"),
    "nota_2": inputs.input_int('nota do aluno'),
    "nota_3": inputs.input_int('nota do aluno'),
}
           
    if aluno1 in alunos:
        print("este nome já está na lista ")
    else:
        alunos.append(aluno1)
        print("nome adicionado ")
        
    for i in alunos:
        
        media = calcular_media(i["nota_1"], i["nota_2"],  i["nota_3"])
        i['media'] = media
        situa1 = verificar_situacao(i["media"]) 
        i['situação'] = situa1
        
    
    
                   
while True:
    print("[1] cadastrar nome")
    print("[2] situação dos alunos")
    print("[3] quantidade de alunos cadastrados")
    print("[4] sair")
    num = input("escolha um numero de 1 a 4")
    if num == "1":
        cadastrar_aluno()
    elif num == "2":
        exibir_todos(alunos)
    elif num == "3":
        print(len(alunos))
    elif num == "4":
        print("sair")
        break
            
             
       
        
    