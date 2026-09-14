a = input()
m = [a]

while a != 'end':
    a = input()
    m.append(a)

print(m)
m = list(map(int, m[:len(m)-1]))
print(m)

x = int(input())

if x in m:
    print(m.index(x))
else:
    print("Число не найдено")