maiorvenda = 0
menorvenda =0
total=0
maiorvenda= 0
menorvenda=300
vendas =0

print("=== Loja 1 ===")
dias = [0,1,2,3,4,5,6,7,8]
for i in range(1,8):
    valor = int(input("vendas do dia: "))

    total += valor 
    vendas +=1

    if valor > maiorvenda:
     maiorvenda = valor

    if valor < menorvenda:
     menorvenda = valor

media = total/vendas
print("--- Resultados da Loja 1 ---")
print("total semanal: ",total)
print("Média Diária: ",media)
print("Dia de maior venda: ",maiorvenda)
print("Dia de menor venda: ",menorvenda)
                            
  
print("=== Loja 2 ===")
dias = [0,1,2,3,4,5,6,7,8]
for i in range(1,8):
    valor = int(input("vendas do dia: "))

    total += valor 
    vendas +=1

    if valor > maiorvenda:
     maiorvenda = valor

    if valor < menorvenda:
     menorvenda = valor

media = total/vendas
print("--- Resultados da Loja 2 ---")
print("total semanal: ",total)
print("Média Diária: ",media)
print("Dia de maior venda: ",maiorvenda)
print("Dia de menor venda: ",menorvenda)

     

    
    


