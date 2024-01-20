numero = int(input("Digite um número: "))
NUM = 32

if numero == NUM:
    print("Você acertou o número")
else:
    print("Você não acertou o número")

#media maior ou igual a 7 = aprovado
#media entre 4 a 6 = recuperação    
#media abaixo de 3 = reprovado
    
numero1 = int(input("Digite a primeira nota: "))
numero2 = int(input("Digite a segunda nota: "))
numero3 = int(input("Digite a terceira nota: "))
numero4 = int(input("Digite a quarta nota: "))

resultado = ((numero1 + numero2 + numero3 + numero4) / 4)

print("A média das notas é de " + resultado)