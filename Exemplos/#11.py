#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("insira um numero qualquer"))
if numero > 0:
    print("Postivo")
elif numero < 0:
    print("negativo")
else :
    print("nulo")