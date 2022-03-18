"""
#Conta a Quantidade de caracteres (len)

usuario = input ('digite o seu usuario: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('voce precisa digitar ao menos 6 caracteres')
else:
    print('voce foi cadastrado no sistema')

#Conta a quantidade de caracteres em uma string
string1 = input('digite alguma coisa: ')
string2 = input('digite outra coisa: ')

print(len(string2))

print(string2.__len__())

#print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')
"""

