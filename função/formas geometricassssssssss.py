


def calcular_quadrado(lado):
    aq = lado**2
    return aq
def calcular_circulo(raio):
    pi = 3.14
    ac = pi * raio**2
    return ac
def calcular_retângulo(base, altura):
    ar = base * altura
    return ar
def calcular_triangulo(lado2):
    raiz = 3
    at = lado2**2 * 3**0.5 / 4
    return at
def calcular_hexagono(at):
    lado3 = 6
    at = lado3**2 * 3**0.5 / 4
    ah = 6 * at
    return ah

    
    
def exibir_n():
    print("Defina dois numeros para efetuar contas basicas")
    print("")
    print("[1] circulo")
    print("[2] quadrado")
    print("[3] retângulo")
    print("[4] triangulo")
    print("[5] hexagono")
    num1 = input("Numero de [1-5]: ")
    print("")
    
    if num1 == "1":
        raio = int(input("solicite o valor do raio"))
        print(calcular_circulo(raio))
        
        
        
    elif num1 == "2":
        lado = int(input("solicite o valor do lado"))
        print(calcular_quadrado(lado))
        
        
        
        
    elif num1 == "3":
        base = int(input("solicite o valor da base"))
        altura = int(input("solicite o valor da altura"))
        print(calcular_retângulo(base, altura))
        
    elif num1 == "4":
        lado2 = int(input("solicitar o valor do lado"))
        print(calcular_triangulo(lado2))
    elif num1 == "5":
        lado3 = int(input("solicite o valor do lado"))
        at= lado3**2 * 3**0.5 / 4
        ah = 6 * at
        print(calcular_hexagono(at))
        
        
def perimetro_circulo(raio2):
    pi = 3.14
    perimetro = raio**2
    perimetro2 = perimetro * pi
    return perimetro2
def permietro_quadrado(lado5):
    pq = lado5 * 4
    return pq
def perimetro_retangulo(base1, altura1):
    pr = 2 * base1 + altura1
    return pr
def perimetro_triangulo(lado6):
    pt = lado6 * 3
    return pt
def perimetro_hexagono(lado7):
    ph = lado7 * 6
    
    
        
def menu_perimetro():
    print("Defina dois numeros para efetuar contas basicas")
    print("")
    print("[1] perimetro do circulo")
    print("[2] perimetro do quadrado")
    print("[3] perimetro do retângulo")
    print("[4] permietro do triangulo")
    print("[5] perimetro do hexagono")
    num2 = input("Numero de [1-5]: ")
    print("")
    
    if num2 == "1":
        raio2 = int(input("solicite o valor do raio"))
        print(perimetro_circulo(raio2))
        
        
    elif num2 == "2":
        lado5 = int(input("solicite o valor do lado"))
        print(perimetro_quadrado(lado5))
    
        
    elif num2 == "3":
        base1 = int(input("solicite o valor da base"))
        altura1 = int(input("solicite o valor da altura"))
        print(perimetro_retangulo(base1, altura1))
        

        
    elif num2 == "4":
        lado6 = int(input("solicite o valor do lado"))
        print(perimetro_triangulo(lado6))
        
    elif num2 == "5":
        lado7 = int(input("solicite o valor do lado"))
        print(perimetro_hexagono(lado7))
    
    
def menus():
    print("selecione o menu desejado")
    print("")
    print("[1] area")
    print("[2] perimetro")
    num3 = input("solicite um numero")
        
    if num3 == "1":
        exibir_n()
        
    elif num3 == "2":
        menu_perimetro()
        
        
menus()
            
        
