### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome


nome_usuario = input("Digite o seu nome: ")

if nome_usuario.isdigit():
    print("Nome errado!!!")
    exit()
elif len(nome_usuario) == 0:
    print("Digite algum caracter &&&&&")
    exit()
elif nome_usuario.isspace():
    print("Vc digitou spacesssss")
    exit()
else:
    print("Nome correto")






# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?