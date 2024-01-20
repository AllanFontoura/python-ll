#enquanto

#saldo = 100

#while(saldo != 0):
#    print("Saldo", saldo)
#    saque = int(input("VALOR SAQUE: "))
#    if(saque <= saldo):
#        saldo = saldo - saque
#    else:
#        print(f"Saldo disponivel {saldo}")

numero_secreto = 82
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("\nTentativa {:02d} de {:02d}".format(rodada,total_de_tentativas))

    tentativa = input("Tente acertar o número de 1 a 100: ")
    print("Você digitou", tentativa)

    tentativa_int = int(tentativa)

    if(tentativa_int <1 or tentativa_int > 100):
        print("Tentativa Inválida! Somente números de 1 a 100!")
        continue

    acerto = tentativa_int == numero_secreto

    if (acerto):
        print("Boa tentativa: ACERTOU!")
        break
    else:
        print("Não foi dessa vez. ERROU!")







    
