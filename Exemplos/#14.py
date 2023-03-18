# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% 
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

def texto():
    salario_novo = salario+(salario*aumento)
    print("salário antes do reajuste : ",salario)
    print("salário depois do reajuste : ",salario_novo)
    print("o percentual de aumento aplicado : ",aumento*100,"%")
    print("o valor do aumento : ",aumento*salario)


salario = float(input("Digite seu Salario : "))
salario_novo = 0
aumento =0

if salario <=280:
    aumento =0.20
    texto()
elif salario < 700:
    aumento =0.10
    texto()
elif salario < 1500:
    aumento =0.15
    texto()
elif salario > 1500:
    aumento =0.05
    texto()