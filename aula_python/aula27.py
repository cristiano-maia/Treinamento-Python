"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = '1000'
texto = 'cristiano'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
outra_variavel2 = f'{texto[:3]}ABC{texto[4:]}'

print(string)

print(outra_variavel)

print(string.zfill(10))

print(texto.capitalize())
print(texto.upper())
print(texto.zfill(50))
print(outra_variavel2)