# 1 - quantos reais sera gastado para fazer uma viagem de 800 km e quantos litros serão necessarios
# 2 - quantos litros são gastados em km na viajem
#quanto de combustivel o carro tem
# descobrir a quantidade de litros que ele tem
# quanto ele ja gastou
#a distancia percorrida
# 3 multiplicar a quantidade que ele tem de gasolina pela autonomia do carro
#somar a distancia que ele tem mais o já percorrido
#subtrair a distancia total pela a já percorrida
#dividir a distancia restante pela a autonimia do carro
#multiplicar o preço pela quantidade de litros



litros_que_tem = 10
distancia_total = 800
preço = 6.90
autonomia_carro = 7
ja_percorrido = 90

km_que_anda_com_o_litros_que_tem = litros_que_tem * autonomia_carro
kilometros_percorridos = km_que_anda_com_o_litros_que_tem + ja_percorrido
distancia_restantes = distancia_total - kilometros_percorridos
quantidade_litros = distancia_restantes/ autonomia_carro
valor = quantidade_litros * preço


print("ele já possui =", km_que_anda_com_o_litros_que_tem)
print("falta percorrer =", distancia_restantes)
print("ele vai gastar em litros =", quantidade_litros)
print("ele vai gastar em R$ =", valor)