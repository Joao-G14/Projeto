valornegativos = 0
valorpositivos = 0
maiorvalor=0
valortotal=0

while valortotal <= 1000:
    valor= int(input())
    if valor ==0:
        continue
    elif valor <0:
     valornegativos += 1
    else: 
     valorpositivos += 1
     valortotal += valor
     if valor > maiorvalor:
        maiorvalor = valor

if valorpositivos > 0:
  media = valortotal/valorpositivos
else:
   media=0



print("total de valores positivos:",valorpositivos)
print("total de valores negativos:",valornegativos)
print("maior valor positivo:", maiorvalor)
print("media dos valores positivos da soma", media)
print("soma final que ultrapassou 1000:", valortotal)



                