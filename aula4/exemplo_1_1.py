"""
Operadores Relacionais - Aula 4
== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""
nome = input("Qual o seu nome? ")
idade = input('Qual a sua idade? ')

idade = int(idade)
# Limite para pegar empréstimo

idade_menor = 20 #muito jovem
idade_maior = 30 #passou da idade



if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome}, empréstimo validado ')
else:
    print(f'{nome}, EMPRÉSTIMO NEGADO ')
