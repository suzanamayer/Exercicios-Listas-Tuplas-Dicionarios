print("Programa para analisar as temperaturas de julho")
print()

# Entrada de dados
print()

datas = []
horas = []
temperaturas = []

arquivo = open("banco-temperaturas-julho.txt", "r")
for linha in arquivo:
    partes = linha.split()
    if len(partes) == 3:
        datas.append(partes[0])
        horas.append(partes[1])
        temperaturas.append(float(partes[2]))
arquivo.close()

# Processamento
total_linhas = len(temperaturas)

soma = 0
for i in range(len(temperaturas)):
    soma += temperaturas[i]

media = soma / total_linhas
minimo = min(temperaturas)
maximo = max(temperaturas)
posicao_minimo = temperaturas.index(minimo)

# Saída de dados
print(f"Total de linhas = {total_linhas}")
print(f"Média das temperaturas = {media:.2f}")
print(f"Temperatura mínima = {minimo:.2f}")
print(f"Temperatura máxima = {maximo:.2f}")
print(f"Primeiro registro da mínima = {datas[posicao_minimo]} às {horas[posicao_minimo]}")

print()