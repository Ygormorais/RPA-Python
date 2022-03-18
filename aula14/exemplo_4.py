"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

#indices
#positivos [012345]
texto = "Python_s2"
#negativos -[987654321]

#fatiamento
nova_string = texto[0::3]
print( nova_string )
"""
#quantidade de caracteres (len)
texto = "python s2"
print( len(texto) )

#imprimir cada letra da sting em uma linha
for letra in texto:
    print(letra)



