ladoA = int(input("Informe o lado A: "))
ladoB = int(input("Informe o lado B: "))
ladoC = int(input("Informe o lado C: "))

if abs(ladoB - ladoC) < ladoA < ladoB + ladoC and\
    abs(ladoA - ladoC) < ladoB < ladoA + ladoC and\
    abs(ladoB - ladoA) < ladoC < ladoB + ladoA:

    if ladoA == ladoB and ladoB == ladoC:
        print("Triângulo Equilátero")
    elif ladoA != ladoB and ladoB != ladoC and ladoA != ladoC:
        print("Triângulo Escaleno")
    else:
        print("Triângulo Isósceles")

else:
    print("As medidas não formam um triângulo")
