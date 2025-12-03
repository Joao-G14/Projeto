maiornota = 0
menornota = 10
acimadamedia = 0
alunos = 0
somanotas= 0
notas = 0
acimadamedia = 0

while True:
    nome =  input("nome do aluno: ")
    notas = int(input("nota do aluno: "))
    if nome == "fim":
        break

    while notas < 0 or notas > 10:
        print("nota invalida,digite um valor")
        notas = int(input("noa do aluno"))

    somanotas += notas
    notas += 1

    if nome == nome:
      alunos += 1

    if notas > maiornota:
     maiornota = notas

    if notas < menornota:
     menornota = notas

    if notas > 6:
     acimadamedia += 1


media = somanotas/notas
print("total de alunos",alunos)
print("media geral",media)
print("maior nota",maiornota)
print("menornota",menornota)
print("alunos acima da media",acimadamedia)



    


