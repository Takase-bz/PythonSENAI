# 1 - o valor que sera cobrado para encher o tanque
# 2 - obter o quanto falta para completar
# obter o valor necessario para completar o tanque
# 3 - subtraia 50 com 20 para saber o valor que sera preenchido
#mutiplique pelo valor do tanque vazio



preço = float(input("solicite o valor da gasolina"))
capacidade_total = int(input("a capacidade total do tanque é de"))
tanque_incompleto = int(input("o tanque esta com"))
capacidade_restante = capacidade_total - tanque_incompleto
pre_encher = capacidade_restante * preço
print(" o valor da gasolina será de =", pre_encher, "R$")


