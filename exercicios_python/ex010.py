"""Calculadora com While"""

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite o perador (+ - / *): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos numeros digitados são invalidos')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue 

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta, confira o resultado abaixo')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float}=', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float}=', num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float}=',num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float}=',num_1_float / num_2_float)

    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im:  ').lower().startswith('s') # variavel minuscula e começa com a letra s
    

    if sair is True:
        break