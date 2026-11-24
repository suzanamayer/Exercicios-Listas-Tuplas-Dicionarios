print("Programa para consultar as temperaturas de um dia")
print()

# Entrada de dados
print()

data = input("Informe uma data (aaaa-mm-dd): ")

print()

datas = []
temperaturas = []

arquivo = open("banco-temperaturas-julho.txt", "r")
for linha in arquivo:
    partes = linha.split()
    if len(partes) == 3:
        datas.append(partes[0])
        temperaturas.append(float(partes[2]))
arquivo.close()

# Processamento
temperaturas_do_dia = []
for i in range(len(datas)):
    if datas[i] == data:
        temperaturas_do_dia.append(temperaturas[i])

# Saída de dados
if len(temperaturas_do_dia) == 0:
    print("A data informada não está presente no arquivo")
else:
    minima = min(temperaturas_do_dia)
    maxima = max(temperaturas_do_dia)
    amplitude = maxima - minima

    print(f"Temperatura mínima = {minima:.2f}")
    print(f"Temperatura máxima = {maxima:.2f}")
    print(f"Amplitude térmica = {amplitude:.2f}")

print()