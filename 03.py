x = int(input("Informe o primeiro número: "))
y = int(input("Informe o segundo número: "))
z = int(input("Informe o terceiro número: "))

if x > y and x > z:
    print('O maior valor é ', x)
elif y > x and y > z:
    print('O maior valor é ', y)
else:
    print('O maior valor é ', z)
