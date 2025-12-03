string = input()
vogais = "aeiou"
contador = 0
for l in string:
    if l not in vogais:
     continue 
    contador += 1
print(f'{contador}')
    