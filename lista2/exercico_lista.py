def exercicio_1():
    lista_inteiros = []
    
    while len(lista_inteiros) < 5:
        while True:
            try:
                numero = int(input("Digite um número para adicionar na lista: "))
                lista_inteiros.append(numero) 
                break
            except:
                print("Você só pode inserir números inteiros")


    for itens in lista_inteiros:
        print(itens)



def exercicio_2():
    lista_inteiros = []
    while len(lista_inteiros) < 5:
        while True:
            try:
                numero = int(input("Digite um número para adicionar na lista: "))
                lista_inteiros.append(numero)
                break
            except:
                print("você só pode inserir números inteiros")

    lista_inteiros.reverse()

    for itens in lista_inteiros:
        print(itens)

def exercicio_3():
    lista_inteiros, lista_par, lista_impar = [], [], []
    while len(lista_inteiros) < 4:
        while True:
            try:
                numero = int(input("Digite um número para adicionar na lista: "))
                lista_inteiros.append(numero)
                if numero % 2 == 0:
                    lista_par.append(numero)
                else:
                    lista_impar.append(numero)
                break
            except:
                print("você só pode inserir números inteiros")

    lista_inteiros_string = str(lista_inteiros).strip('[]')
    print("A lista de números é: " + lista_inteiros_string)
    
    lista_pares_string = str(lista_par).strip('[]')
    print("Os pares são: " + lista_pares_string)

    lista_impares_string = str(lista_impar).strip('[]')
    print("Os impares são: " + lista_impares_string)

def exercicio_4():
    soma = 0 
    lista_inteiros = []
    while len(lista_inteiros) < 10:
        numero = float(input("Digite um número para adicionar na lista: "))
        lista_inteiros.append(numero)
        
    for item in lista_inteiros: 
        soma = float(soma + item)
    media = soma / len(lista_inteiros)

    print("A soma da lista é: %.2f " % soma)
    print("A média é %.2f" % media)

exercicio_4()
