def nome_sobrenome():

    name = input("coloca seu nome kraio: ")
    sobrenome = input ("sobrenome agora: ")
    print(name + " " + sobrenome )

def soma_numeros():
    numero1 = int(input("digite um número: ")) 
    numero2 = int(input("digite outro número: "))
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


