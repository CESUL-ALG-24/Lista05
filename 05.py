consumo = int(input("Informe o consumo em m3: "))

valor_fatura = 34.49

# 34,49
# 5,35
# 29,7
# 29,85
# 30,1


# Calcula o que passou da taxa básica (5m)
excedente = consumo - 5

if excedente > 0:

    # Faixa 1 - 6 a 10m3
    if excedente <= 5:
        valor_fatura += excedente * 1.07
    else:
        #Faixa 2 - 11 a 15
        valor_fatura += 5 * 1.07
        excedente -= 5

        if excedente <= 5:
            valor_fatura += excedente * 5.94
        else:
            #Faixa 3 - 16 a 20
            valor_fatura += 5 * 5.94
            excedente -= 5

            if excedente <= 5:
                valor_fatura += excedente * 5.97
            else:
                # Faixa 4 - 21 a 30
                valor_fatura += 5 * 5.97
                excedente -= 5

                if excedente <= 10:
                    valor_fatura += excedente * 6.02
                else:
                    # Faixa 5 - Acima de 30
                    valor_fatura += 10 * 5.97
                    excedente -= 10

                    valor_fatura += excedente * 10.19

print("O valor a pagar será R$:", valor_fatura)
