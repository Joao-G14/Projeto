notas = []

for i in range(5):
    n = int(input("Digite a nota: "))
    notas.append(n)

# soma manual
total = 0
for n in notas:
    total += n

# maior e menor
maior = notas[0]
menor = notas[0]
for n in notas:
    if n > maior:
        maior = n
    if n < menor:
        menor = n

# filtrar notas acima de 70
acima_de_70 = [n for n in notas if n > 70]

print("Notas:", notas)
print("Soma:", total)
print("Maior:", maior)
print("Menor:", menor)
print("Notas acima de 70:", acima_de_70)