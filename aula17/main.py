#   Índices
#   0123456789...................33

"""Imprimir na tela quantos caracteres tem a frase digitada na variavel
print(tamanho_frase)
"""
frase = 'o rato roeu a roupa do rei de roma' #Valor Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_usuario = input('Qual letra deseja colocar maiuscula: ')

#Iteração < Iterar
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)
