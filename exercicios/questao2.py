total = 0
abaixodamedia = 0
alta = 0
baixa = 100
somanotas=0
sequenciaatual=0
maiorsequencia=0

for i in range(15):
    notas = int(input())

    while notas < 0 or notas > 100:
      print("nota invalida,digita um valor")
      notas = int(input())

    total += notas
    somanotas += 1


    if notas > alta:
     alta = notas

    if notas < baixa:
     baixa = notas

    if notas < 50:
     abaixodamedia += 1
         
    if notas >= 80:
        sequenciaatual += 1
        if sequenciaatual > maiorsequencia:
            maiorsequencia = sequenciaatual
    else:
        sequencia_atual = 0 

media = total/somanotas
print("total de pontos obitidos no semestre:",total)
print("quantas semanas ficaram abaixo da media",abaixodamedia)
print("nota mais baixa:",baixa)
print("nota mais alta",alta)
print("maior sequencia:",maiorsequencia)
print("media:",media)

               
      


