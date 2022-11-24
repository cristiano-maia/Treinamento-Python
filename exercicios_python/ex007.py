"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


entrada = input('Digite a hora em numero inteiro: ')

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print(f'Hora digitada {entrada} --> Bom dia')

    elif hora >= 12 and hora <= 17:
        print(f'Hora digitada {entrada} --> Boa tarde')

    elif hora >= 18 and hora <= 23:
        print(f'Hora digitada {entrada} --> Boa noite')

    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')