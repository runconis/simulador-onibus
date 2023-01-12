from random import randint

passageiros = 0
soma = 0

def subida():
    global parada
    global passageiros
    global soma
    x = randint(0, 10)
    if passageiros == 40:
        print('O ônibus está na lotação máxima, com 40 passageiros! Ninguém pode embarcar.')
    elif (passageiros + x) > 40:
        print('Quantidade de passageiros que embarcaram:', (40 - passageiros))
        soma += (40 - passageiros)
        passageiros = 40
    else:
        passageiros += x
        soma += x
        print('Quantidade de passageiros que embarcaram:', x)

def descida():
    global parada
    global passageiros
    x = randint(0, 10)
    if passageiros == 0:
        print('Não há nenhum passageiro para desembarcar.')
    elif passageiros <= x or parada == 20:
        print('Quantidade de passageiros que desembarcaram:', passageiros)
        passageiros = 0
    else:
        passageiros -= x
        print('Quantidade de passageiros que desembarcaram:', x)

for parada in range(1, 21):
    print()
    print('Parada número', parada)
    if parada == 1:
        print('Início da linha!')
        subida()
    elif parada == 20:
        print('Fim da linha!')
        print('Quantidade de passageiros ao chegar na parada:', passageiros)
        descida()
        print(f'Foi transportado um total de {soma} passageiros!')
    else:
        print('Quantidade de passageiros ao chegar na parada:', passageiros)
        descida()
        subida()