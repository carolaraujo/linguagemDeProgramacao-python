# Troca Variáveis
# O codigo para a entrada de dados e impressao
# dos resultados eh dado.
v1 = input()
v2 = input()

# insira na janela abaixo o codigo responsavel por
# trocar os valores de uma variavel para a outra
v3 = v1
v1 = v2
v2 = v3

print('valor em v1:', v1)
print('valor em v2:', v2)

# Média Simples
alt1 = float(input())
alt2 = float(input())
alt3 = float(input())
alt4 = float(input())

media = (alt1 + alt2 + alt3 + alt4)/4

print('A media das alturas eh:', media)

# Escala de Temperatura
numero = float(input())

t_celsius = (numero-32) * 5/9
t_kelvin = t_celsius + 273.15

print("Convertendo", numero, "graus Fahrenheit temos:")
print(t_celsius, "graus Celsius e", t_kelvin, "Kelvin")

# Conversão polegadas -> mm
polegadas = float(input())

m = polegadas * 25.4

print(polegadas, "polegada(s) eh o mesmo que", m, "mm")