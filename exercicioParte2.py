# Um fabricante vendeu 120 unidades de um produto que custa R$ 40,00 cada
# Sobre o valor vendido, o fabricante paga 40% de imposto. Escreva um programa
# que calcule o valor do imposto a ser pago

valor_original = float(input("valor original: R$ "))
desconto = float(input("Desconto (em %) para esse produto: "))
desconto = desconto / 100
print("valor original:    R$", valor_original)
print("Desconto ganho:    R$", valor_original * desconto)
print("valor com desconto:    R$", valor_original * (1-desconto))

# Escreva um programa que calcule o rendimento em km/l de um automóvel
# Sendo dados: a quantidade de litros de combústivel gasta é igual a 43 litros
# e a distância percorrida é igual a 473km
distancia = 473
litros = 43
print(distancia * litros)