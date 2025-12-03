maiorvenda = 0
menorvenda =0
total=0
maiorvenda= 0
menorvenda=300
vendas = 0
diamaior = ""
diamenor = ""

loja = range(1,10000000000)
for i in loja:
 print(f"=== Loja {i}===")

 dias = ["domingo","segunda","terça","quarta","quinta","sexta","sabado"]
 for i2 in dias:
    valor = int(input(f"vendas de{i2}: "))

    total += valor 
    vendas +=1

    if valor > maiorvenda:
     maiorvenda = valor
     diamaior = i2
    if valor < menorvenda:
     menorvenda = valor
     diamenor = i2
     
 media = total/vendas
 print("--- Resultados da Loja 1 ---")
 print("total semanal: ",total)
 print("Média Diária: ",media)
 print("Dia de maior venda: ",diamaior,maiorvenda)
 print("Dia de menor venda: ",diamenor,menorvenda)


