from math import *
def soma(a=0, b=0):
    som = a + b
    return print(f'Somando os valores: {a} + {b}, temos {som}.')

def subtração(a=0, b=0):
    sub = a - b
    return print(f'A subtraindo os valores: {a} - {b}, temos {sub}.')

def multiplicação(a=1, b=1):
    mult = a * b
    return print(f'A multiplicando os valores: {a} x {b}, temos {mult}')

def divisão(a=1, b=1):
    div = a / b
    return print(f'Dividindo os valores: {a} / {b}, temos {div}')

def fact(a=1):
    return print(f'O factorial de {a} é {factorial(a)}')

def raizquadrada(a=0):
    return print(f'A raiz quadrada de {a} é igual a {sqrt(a)}')

def pip():
    return print(f'O valor do pi é igual a {pi()}')

def cabeçalho(msg):
    print('~' * 45)
    print(f'{msg}'.center(45))
    print('~' * 45)

def linha():
    print('~' * 45)

cabeçalho('PyCalculator')
print('''Escolha uma das opções:
1 - Soma
2 - Subtração
3 - Divisão
4 - Factorial
5 - Raiz Quadrada
6 - Valor de pi
7 - multiplicação
''')
linha()
while True:
    try:
        opc = int(input('O que você escolhe? '))
        if opc == 1:
            a = int(input('Primeiro número: '))
            b = int(input('Segundo número: '))
            soma(a, b)
        elif opc == 2:
            a = int(input('Primeiro número: '))
            b = int(input('Segundo número: '))
            subtração(a, b)
        elif opc == 3:
            a = int(input('Primeiro número: '))
            b = int(input('Segundo número: '))
            divisão(a, b)
        elif opc == 4:
            a = int(input('Digite um número: '))
            fact(a)  
        elif opc == 5:
            a = int(input('Digite um número: '))
            raizquadrada(a)
        elif opc == 6:
            pip()
        elif opc == 7:
            a = int(input('Primeiro número: '))
            b = int(input('Segundo número: '))
            multiplicação(a, b)
        else:
            print('Por favor, digite apenas os números disponíveis nas opções!')
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'N':
            break
    except ValueError:
        print(f'Erro, Digite os valores correctamente!')
linha()
print('««««Programa Finalizado»»»»')