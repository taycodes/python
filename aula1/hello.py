def lista():
    nome = input("digite o seu nome:")
    idade = input("digite sua idade:")
    resultado = nome + " tem " + idade + " anos "
    print(resultado)

def par(rangeNumbers):
    for number in range(rangeNumbers):
        if number % 2 == 0:
            print(number)

print("oi")

lista() 
par(100)           