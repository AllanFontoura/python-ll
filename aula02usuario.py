class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

login = Usuario(input("Digite seu Nome: "), input("Digite a senha: "))

print("\nDados para Realizar o Login:")
nome1 = (input("Digite seu nome: "))
senha1 = (input("Digite sua senha: "))

if(nome1 == login.nome and senha1 == login.senha):
    print("Usuário autenticado com sucesso.")
    print("Olá",login.nome, ". \nSeja Bem Vindo")
else:
    print("Nome ou senha Incorreto")

        
