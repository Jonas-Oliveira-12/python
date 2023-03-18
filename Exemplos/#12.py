#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Insira F para feminino e M para masculino")
if sexo.upper() == "F":
    print("feminino")
elif sexo.upper() == "M":
    print("masculino")
else:
    print("sexo invalido")