from enum import Enum

class InputType(Enum):
    STR = 0 
    INT = 1
    FLOAT = 2

def validar_input(valor):
    if valor.isnumeric():
        return True
    else:
        print("Você precisa digitar um número")
        return False

def custom_input(tipo: InputType, titulo: str):
    
    if tipo == InputType.INT:
        is_error = True
        numero_inteiro = 0
        
        while(is_error):
            numero_str = input(titulo)
            
            if validar_input(numero_str):
                is_error = False
                numero_inteiro = int(numero_str)        

            else:
                is_error = True
        
        return numero_inteiro                

    elif tipo == InputType.FLOAT:
        is_error = True
        while(is_error):
            numero_real = input(titulo)
            if validar_input(numero_real):
                is_error = False
                return float(numero_real)

    else:
        return input(titulo) 


def nome_sobrenome():

    name = custom_input(InputType.STR, "coloca seu nome kraio: ")
    sobrenome = input ("sobrenome agora: ")
    print(name + " " + sobrenome )

def soma_numeros():
    numero1 = custom_input(InputType.INT, "Digite um número: ")
    numero2 = custom_input(InputType.INT, "Digite outro número: ")
    print(numero1 + numero2)

def diferenca_numeros():
    numero1 = int(input("digite um número: "))
    numero2 = int(input("digite um número: "))

    while numero2 > numero1: 
        print("número inválido, digite um número igual ou menor que o primeiro")
        numero2 = int(input("digite um número: "))
    print(numero1 - numero2)

def kilos():
    quilogramas = float(input("valor kg: "))
    gramas = quilogramas * 1000 
    print("gramas: %.2fg " % gramas)

def inflacao():
    preco_atual = float(input("digite preço atual do produto: "))
    preco_antigo = float(input("digite o preço antigo do produto: "))
    variacao = ((preco_atual - preco_antigo) / preco_antigo) * 100
    print("variacao: %.2f%% " % variacao)

def calcular_desconto():
    preco_mercadoria = float(input("digite o preço da mercadoria: "))
    desconto = float(input("percentual de desconto: "))
    valor_desconto = (preco_mercadoria * (desconto / 100 ))
    valor_produto = (preco_mercadoria - valor_desconto)
    print(f"Valor do desconto: { valor_desconto }\nValor do produto: { valor_produto }")

soma_numeros()    
                    
