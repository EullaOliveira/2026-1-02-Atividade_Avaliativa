import random

x = 0
repeticoes = int(input('Digite a quantidade de números aleatórios: '))

for x in range(x, repeticoes, 1):
    numero_aleatorio = random.randint(1, 100)
    print(f'{x}° número aleatório {numero_aleatorio}')