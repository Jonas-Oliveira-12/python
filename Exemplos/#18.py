#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

numero = 0
while numero != 50:
    numero += 1
    if numero % 2 != 0:
        print("numero impar : ",numero)
    else:
        print("numero par : ",numero)