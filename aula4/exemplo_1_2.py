"""
Operadores Lógicos - Aula 4
and, or, not
in e not in
------------------------------------------------------------------------------------------------------------------
(Verdadeiro e Verdadeiro) = Verdadeiro - as duas afirmações precisam verdadeiras
comparacao1 and comparacao
---------------------------------------------------------------------------------------------------------
comp1 or comp
# Verdadeiro ou Verdadeiro - Só precisa de uma afirmação verdadeira
----------------------------------------------------------------------------------------------------------------
a = ''
b = 0
if not b:
    print("Por favor, preencha o valor de B")

#(NOT) Inverte a afirmação
------------------------------------------------------------------------------------------------
nome = 'ygor'
if 'alberto' not in nome:
    print("Existe")
else:
    print("Não existe")

#(NOT IN) Inverte a afirmação
---------------------------------------------


"""

usuario = input('Nome de usuário: ')
senha = input('Senha de usuário: ')

usuario_bd = 'ygor'
senha_bd = '2712'

if usuario_bd ==  usuario and senha_bd == senha:
    print('Login efetuado com sucesso.')
else:
    print('Usuário ou senha inválidos.')

    






