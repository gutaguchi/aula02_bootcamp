import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# valor01 = int(input("valor 01 = "))
# valor02 = int(input("valor 02 = "))
# total = valor01 + valor02
# print(total)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# valor03 = int(input("valor 03 = "))
# resto = valor01%5
# print(resto)


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# num01 = float(input("Digite o numero 01 = "))
# num02 = float(input("Digite o numero 02 = "))
# resultado = num01*num02
# print(resultado)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#
# try:
#     num1 = int(input("num 01 = "))
#     num2 = int(input("num 02 = "))
#     resultado = num1 // num2
#     print(resultado)
# except ZeroDivisionError:
#     print("integer division or modulo by zero")
# except KeyboardInterrupt:
#     print("Someone interrupted the keyboard")
# except TypeError as e:
#     print(e)
# else:
#     print("ocorreu tudo bem")
# finally:
#     print("Muito bem")
    #

# numero = int(input("Insira um numero: "))
# if isinstance(numero, int):
#     print("é inteiro")
# else:
#     print("nao é inteiro")





# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num01 = float(input("Digite o numero 01 = "))
# quadrado = num01**2
# print(quadrado)


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# num01 = float(input("Digite o numero 01 = "))
# num02 = float(input("Digite o numero 02 = "))
# resultado = num01+num02
# print(resultado)
# print(f"{resultado:.2f}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# num01 = float(input("Digite o numero 01 = "))
# num02 = float(input("Digite o numero 02 = "))
# resultado = (num01+num02)/2
# print(resultado)


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# resultado = pow(2,3)
# print(resultado)


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# def celsius_para_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# # Solicita ao usuário a temperatura em Celsius
# temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

# # Converte para Fahrenheit
# temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)

# # Exibe o resultado
# print(f"{temperatura_celsius}°C equivale a {temperatura_fahrenheit:.2f}°F")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.


# raio = int(input("raio = "))
# area = math.pi * raio ** 2
# print(f"{area:.2f}")


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

#data = input("insira uma data formato dd/mm/aaaa: ")
#lista_data = data.split("/")
#print(lista_data)
#print(f"numero lista 2 : {lista_data[1]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# num01 = int(input("Digite o numero 01: "))
# num02 = int(input("Digite o numero 02: "))
# if num01 == num02:
#     print("Numeros iguais")
# else:
#     print("Numeros diferentes")


# #### try-except e if

# 21: Conversor de Temperatura


# while True:
#     try:
#         temperatura = float(input("Digite uma tempetura em Fahrenheit: "))
#         print(f"A temperatura digitada é {temperatura}")
#         resultado = ((temperatura - 32)/9)*5
#         print(f"O resultado de Fahrenheit para Celsius é {resultado}")
#         if isinstance(temperatura, int) == True or isinstance(temperatura, float) == True:
#             break
#     except ZeroDivisionError:
#         print("Divisao por zero nao eh possivel!!!")
#     except ValueError:
#         print("Digite um valor válido!!!")
#     except:
#         print("Erro inesperado")
#     finally:
#         print("Sempre executa")





# try:
#    int_value = int(value)
# except (TypeError, ValueError):
#     print('Not an integer')


# except isinstance(temp, int):
#     print("é inteiro")
# except TypeError as e:
#     print(e)
# except ValueError:
#     raise print("Náo é inteiro")

# s = "123"
# try:
#   i = int(s)
# except ValueError as verr:
#   pass # do job to handle: s does not contain anything convertible to int
# except Exception as ex:
#   pass # do job to handle: Exception occurred while converting to int

# try:
#     nome = input("Digite seu nome: ")

#     # Verifica se o nome está vazio
#     if len(nome) == 0:
#         raise ValueError("O nome não pode estar vazio.")
#         exit()
#     # Verifica se há números no nome
#     elif any(char.isdigit() for char in nome):
#         raise ValueError("O nome não deve conter números.")
#         exit()
#     else:
#         print("Nome válido:", nome)
# except ValueError as e:
#     print(e)
#     exit()


# 22: Verificador de Palíndromo
# 23: Calculadora Simples
try:
    num01 = float(input("Digite o primeiro numero: "))
    num02 = float(input("Digite o segundo numero: "))
    operador = input("Digite o operador: ")
    print(num01)
    print(num02)
    print(operador)
    if operador == "+":
        resultado = num01 + num02
    elif operador == "*":
        resultado = num01 * num02
    elif operador == "/":
        resultado = num01 / num02 
    print(resultado)
except ZeroDivisionError:
    print("Nao pode dividir por zero")




# 24: Classificador de Números
# 25: Conversão de Tipo com Validação



# try:
#     num1 = int(input("num 01 = "))
#     num2 = int(input("num 02 = "))
#     resultado = num1 // num2
#     print(resultado)
# except ZeroDivisionError:
#     print("integer division or modulo by zero")
# except KeyboardInterrupt:
#     print("Someone interrupted the keyboard")
# except TypeError as e:
#     print(e)
# else:
#     print("ocorreu tudo bem")
# finally:
#     print("Muito bem")