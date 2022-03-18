nome = 'Ygor Alberto' #string
idade = 19 #int
altura = 1.64 #float
e_maior = idade > 18 #bool
peso = 83
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print ('{n} tem {i} anos de idade e seu imc é {im}'.format(n = nome, i = idade, im =  imc))


