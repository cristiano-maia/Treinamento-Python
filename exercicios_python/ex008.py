"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome >=3:
    if tamanho_nome <=4:
        print(f'Nome: {nome}')
        print(f'Letras: {tamanho_nome}')
        print(f'Seu nome é curto')

    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print(f'Nome: {nome}')
        print(f'Letras: {tamanho_nome}')
        print(f'Seu nome é normal')
    
    else:
        print(f'Nome: {nome}')
        print(f'Letras: {tamanho_nome}')
        print(f'Seu nome é grande')

else:
    print(f'Nome: {nome} --> Digite mais de dois caracteres')