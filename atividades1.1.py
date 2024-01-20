numerou = int(input("Digite a primeira nota: "))
numerod = int(input("Digite a segunda nota: "))
numerot = int(input("Digite a terceira nota: "))
numeroq = int(input("Digite a quarta nota: "))

resultado = ((numerou + numerod + numerot + numeroq) / 4)

print ("Sua média é de", resultado, "a sua situação é:")

if (resultado >= 7):
    print("Aprovado")     
elif (resultado >=4): #media >= 4 or media <=6
    print("Recuperação")
else: 
    print("Reprovado")

