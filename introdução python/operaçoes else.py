num1 = int(input("solicite um numero"))
num2 = int(input("solicite um numero"))

operação = input("digite a operação desejada (+, -, *, /)")

if operação == "+":
    print(num1 + num2)


elif operação == "-":
    print(num1 - num2)


elif operação == "*":
    print(num1 * num2)


elif operação == "/":
    print(num1 / num2)
    
else:
    print("operação desconhecida")