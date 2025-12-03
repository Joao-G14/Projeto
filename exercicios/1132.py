x = int(input())
y = int(input())

if x > y:
    x, y = y, x

soma = 0
n = x

while n <= y:
    if n % 13 != 0:
        soma += n
    n += 1

print(soma)
