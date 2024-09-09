#Crie um programa que converta uma temperatura dada em Celsius para Fahrenheit usando a fórmula: F = C * 9/5 + 32.

c = float(input("digite a temperatura em celsius;"))
f = 32 + (9/5)*c
k = c + 273
print("a temperatura em celsius é:",c,"°c")
print("a tenperatura em fahrenheit é:",f,"°f")
print("a tenperatura em kelvin é:",k,"k")