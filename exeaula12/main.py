"""
Faça um programa que peça ao user para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o user nao digite um numero
inteiro, informe que nao é um numero inteiro.
"""
#numero_inteiro = input('digite um numero inteiro: ')
#
#if numero_inteiro.isdigit():
#   numero_inteiro = int(numero_inteiro)
#
#   if numero_inteiro % 2 == 0:
#       print(f"{numero_inteiro} é par")
#    else:
#        print(f"{numero_inteiro} é impar")
#else:
#   print('Isso nao é um numero inteiro')

"""
Faça um programa que pergunte a hora user e, baseando-se no horario
descrito, exiba a saudaçao apropriada.
Bom dia 00:00 as 11, Boa-Tarde 12:00 as 17:00 e Boa-Noite das 18:00 as 23:00 horas.
"""
#horario = input('digite um horario (0-23): ')
#
#if horario.isdigit():
#    horario = int(horario)
#
#    if horario < 0 or horario > 23:
#        print("Horario deve estar entre 0 e 23.")
#    else:
#        if horario <= 11:
#            print("bom dia")
#        elif horario <= 17:
#            print("boa tarde")
#        else:
#            print("boa noite")
#else:
#    print("Por favor digite um horario entre 0 e 23.")

"""
Faça um programa que peça o primeiro nome do usuario. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto demais";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 "Seu nome é muito grande".
"""

nome = input("digite seu nome: ")
tamanho = len(nome)

if tamanho <= 4:
    print("seu nome é curto demais")
elif tamanho <= 6:
    print("seu nome é normal")
else:
    print("seu nome é grande demais")


