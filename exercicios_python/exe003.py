# Crie um programa que leia dois valores e qual variavel recebeu o maior valor

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual'
        f'do que {segundo_valor=}'
    )
else:
   print(
        f'{segundo_valor=} é maior ou igual'
        f'do que {primeiro_valor=}'
    )