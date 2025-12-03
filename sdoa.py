maiorvenda = 0
menorvenda =0
total=0
maiorvenda= 0
menorvenda=300
vendas = 0
diamaior = ""
diamenor = ""

maior_total = -999999999
menor_total = 999999999
loja_maior = 0
loja_menor = 0

loja = int(input("quantidade de lojas: "))
for i in range(1, loja + 1):
 print(f"=== Loja {i}===")

 dias = ["domingo","segunda","terça","quarta","quinta","sexta","sabado"]

 total = 0
 vendas = 0
 maiorvenda = 0
 menorvenda = 300
 
 for i2 in dias:
    valor = int(input(f"vendas de {i2}: "))

    total += valor 
    vendas +=1

    if valor > maiorvenda:
     maiorvenda = valor
     diamaior = i2
    if valor < menorvenda:
     menorvenda = valor
     diamenor = i2
     
 media = total/vendas
 print(f"--- Resultados da Loja {i} ---")
 print("total semanal: ",total)
 print("Média Diária: ",media)
 print("Dia de maior venda: ",diamaior,maiorvenda)
 print("Dia de menor venda: ",diamenor,menorvenda)


 if total > maior_total:
    maior_total = total
    loja_maior = i

 if total < menor_total:
    menor_total = total
    loja_menor = i

print("\n===== RESULTADO FINAL =====")
print("Loja com MAIOR total semanal:", loja_maior, "com total de", maior_total)
print("Loja com MENOR total semanal:", loja_menor, "com total de", menor_total)

