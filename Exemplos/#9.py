#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete
#A mensagem "Reprovado", se a média for menor do que sete
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a nota 1º : "))
nota2 = float(input("Digite a nota 2º : "))
nota3 = float(input("Digite a nota 3º : "))
nota4 = float(input("Digite a nota 4º : "))
media = (nota4+nota3+nota2+nota1)/4
print("A média das suas notas é : ",media)
if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")