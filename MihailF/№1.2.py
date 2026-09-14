n = int(input())  # сколько чисел Фибоначчи нужно внести в массив
a = []

x, y = 1, 1
for i in range(n):
    a.append(x)
    x, y = y, x + y

print(a)