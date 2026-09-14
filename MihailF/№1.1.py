a=input()
b=input()
op=input()

if b!= "0" and op != "/":
    print(eval(str(a) + op + str(b)))

#2-вариант

a, op, b = input().split()
print(a, op, b, "=", eval(a + op + b)) #вывод: 2 + 3 = 5