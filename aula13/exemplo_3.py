"""
formatando valores com modificadores - aula 5

:s - texto (strings)
:d - inteiro (int)
:f - numeros de ponto flutuante (float)
:.(NÚMERO)f - quantidade de casas decimais (float) - :.2f
:(CARACTERE) (> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - esquerda
< - direita
^ - centro
"""

num1 = 10
num2 = 3
divisao = num1 / num2
print( '{:.2f}'.format(divisao))

#maneira de se chegar ao mesmo resultado usando (fstrings)
#print( f'{divisao:.2f}')
