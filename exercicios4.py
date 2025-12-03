# =====================================================
# Resumo de loops, listas, range e manipulação de dados
# =====================================================

# 1️⃣ Armazenando valores em uma lista e validando entradas
valores = []  # vetor vazio
num_entradas = 5  # exemplo de quantidade de entradas

for i in range(num_entradas):
    while True:  # loop de validação
        n = int(input(f"Digite o valor {i+1}/{num_entradas} (0-100): "))
        if 0 <= n <= 100:
            valores.append(n)  # adiciona à lista
            break
        else:
            print("Valor inválido! Tente novamente.")

# 2️⃣ Soma manual
total = 0
for v in valores:
    total += v

# 3️⃣ Maior e menor valores manualmente
maior = valores[0]
menor = valores[0]
for v in valores:
    if v > maior:
        maior = v
    if v < menor:
        menor = v

# 4️⃣ Média
media = total / len(valores)

# 5️⃣ Contagem de valores acima de 70
acima_de_70 = 0
for v in valores:
    if v > 70:
        acima_de_70 += 1

# 6️⃣ Maior sequência consecutiva acima de 50
seq_atual = 0
maior_seq = 0
for v in valores:
    if v > 50:
        seq_atual += 1
        if seq_atual > maior_seq:
            maior_seq = seq_atual
    else:
        seq_atual = 0

# 7️⃣ Filtragem de valores (list comprehension)
valores_filtrados = [v for v in valores if v >= 60]

# 8️⃣ Ordenando a lista
valores_ordenados = sorted(valores)  # crescente
valores_ordenados_desc = sorted(valores, reverse=True)  # decrescente

# 9️⃣ Saída resumida
print("\n===== RESUMO =====")
print("Valores digitados:", valores)
print("Total:", total)
print("Média:", media)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Quantidade acima de 70:", acima_de_70)
print("Maior sequência acima de 50:", maior_seq)
print("Valores filtrados >= 60:", valores_filtrados)
print("Valores ordenados:", valores_ordenados)
print("Valores ordenados desc:", valores_ordenados_desc)

# =========================
# Fim do resumo de loops e listas
# =========================
