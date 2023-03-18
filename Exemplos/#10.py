#Faça um Programa que leia três números e mostre o maior deles.

num1 = int(input("Insira um numero qualquer : "))
num2 = int(input("Insira outro numero qualquer : "))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("os numeros sao iguas")