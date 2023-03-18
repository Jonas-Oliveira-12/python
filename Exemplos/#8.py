#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

num1 = int(input("Insira um numero inteiro"))
num2 = int(input("Insira outro numero inteiro"))
num3 = float(input("Insira outro numero real"))

a = (2*num1) * (num2/2)
b = (3*num1) + num3
c = num3**3

print(a,"\n",b,"\n",c,"\n")