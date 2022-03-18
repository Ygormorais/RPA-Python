"""
#isnumeric, isdigit, isdecimal (convertem string para int)
#checa se a string tem numeros e positivos
print(num1.isnumeric())
print(num2.isnumeric())

num1 = input('Digite um numeoro: ')
num2 = input('Digite outro numero: ')

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Nao pude converter os numeros para realizar contas')
"""
#contornar erros quando nao se sabe o que será inputado pelo user!
num1 = input('digite um numero: ')
num2 = input('digite outro numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')