numero = int(input('Digite um número: '))
divisores = []
i = 0

for i in range(i, numero-1, 1):
    i+=1
    if numero % i == 0:
        divisores.append(i)

somadivisores = sum(divisores)

if somadivisores == numero:
    print(f'{numero} é perfeito.')
else:
    print(f'{numero} não é perfeito.')