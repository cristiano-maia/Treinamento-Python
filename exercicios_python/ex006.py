"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

entrada = input('Digite um número: ')

if entrada.isdigit():
    situacao = int(entrada) % 2
    situacao == 0
    print(f'Numero digitado {entrada} é PAR')

elif entrada.isdigit():
    situacao = int(entrada) % 2
    situacao == 1
    print(f'Numero digitado {entrada} é IMPAR')

else:
    print(f'Você não digitou um numero inteiro')