numero = int(input("Digite um número para saber se ele é Primo ou não\n Numero: "))
if numero >1:
    for sobra in range(2, numero):
        if numero % sobra == 0:
            print (numero, "não é um número primo")
            break
        else:
            print(numero, " um número primo")
            break
            
            