numero = int(input('Digite um número: '))
copia_numero = numero
i = 0

if copia_numero == 0:
    digitos = 1
else:
    digitos = 0
    for i in range(100):
        if copia_numero> 0:
            digitos += 1
            copia_numero //=10
        else:
            break
print(digitos)