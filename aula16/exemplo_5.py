"""
While /  Else - Aula 8
contadores
acumuladores
"""
contador = 1
acumulador = 1


while contador <= 10:
    print(contador, acumulador)

#QUEBRANDO O LAÇO COM O IF E BREAK
    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')
    #APÓS QUEBRA DO LAÇO, EXIBIRÁ ESSA MENSAGEM NA TELA
print('isso aqui será executado fora do laço')