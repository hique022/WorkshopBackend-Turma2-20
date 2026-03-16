notas = [7, 6, 9]
pesos = [1, 2, 1]

soma = 0
soma_pesos = 0

for i in range (len(notas)):
    soma = soma + notas [i] * pesos[i]
    soma_pesos = soma_pesos + pesos[i]

media = soma / soma_pesos

print("A media ponderada é :",media)