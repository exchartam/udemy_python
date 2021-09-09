"""
# 01
print('Insira dois números para descobrir qual é maior.')
num1 = input('Insira o primeiro número: ')
num2 = input('Insira o segundo outro número: ')

if num1 > num2:
    print('O primeiro número é maior!')
elif num1 == num2:
    print('Os números são iguais!')
else:
    print('O primeiro número é menor!')

# 02

num3 =float(input('Insira um número para descobrir sua raiz quadrada: '))
num4 = num3 ** (1/2)

if num3 >= 0:
    print(f'A raiz quadrada é: {num4}')
else:
    print("O número é inválido.")

# 03

num3 = float(input('Insira um número para descobrir sua raiz quadrada e seu valor ao quadrado: '))
num4 = (int(num3) ** (1/2))
num5 = (int(num3) ** 2)

if num3 >= 0:
    print(f'A raiz quadrada é: {num4}')
else:
    print(f'O número digitado ao quadrado é: {num5}')


#05

num3 = float(input('Insira um número para descobrir se é par ou ímpar: '))
num4 = (num3 % 2)

if num4 == 0:
    print(f'O número é par')
else:
    print(f'O número é ímpar')


#08

nota1 = float(input("Insira a nota da 1ª avaliação: "))
nota2 = float(input("Insira a nota da 2ª avaliação: "))

if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = float((nota1+nota2) / 2)
    print(f"A média das notas é: {media}")
else:
    print("Todos os valores precisam estar entre 0 e 10!")

#09

salario = float(input("Insira o salário: "))
prestacao = float(input("Insira o valor da prestação: "))
percentual = float((prestacao/salario)*100)


if salario > 0 and prestacao > 0:
    if percentual <= 20:
        print(f"Empréstimo concedido:  {percentual} %")
    else:
        print(f"Empréstimo rejeitado:  {percentual} %")
else:
    print("Valores negativos são rejeitados.")

#10
sexo = input("Selecione H para homens e M para mulheres: ")
altura = float(input("Altura: "))
pesoh = 72.7 * altura - 58
pesom = 62.1 * altura - 44.7

if sexo == "H":
    print(f'Seu peso ideal é: {pesoh}')
elif sexo == "M":
    print(f"Seu peso ideal é: {pesom}")
else:
    print("Digite corretamente M ou F")

#11

num = int(input("Insira um número: "))
num2 = list(str(num))
num3 = list(map(int, num2))
num4 = sum(num3)

print(num4)

if num > 0:
    print(f"Soma de todos os algarismos: {num4}")
else:
    print("Número Inválido")

"""
