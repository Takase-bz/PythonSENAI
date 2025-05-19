
#comprimento do lado do hexágono e devolver a área correspondente.
#HEXAGONO = Ah = 6 * At
#TRIANGULO EQUILATERO At=l2*√3 /4

numero_lados = int(input("cite um numero para o lado do triangulo = "))

triangulo_2 = numero_lados * numero_lados
raiz = 3**0.5
triangulo_3 = triangulo_2 * raiz
resultado_1 = triangulo_3 / 4
print("Area do triangulo =  ",resultado_1)

area_hexagono = 6 * resultado_1
print("a area do hexagono é de =", area_hexagono)
