def validacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    elif imc >= 30 and imc < 35:
        return "Obesidade grau 1"
    elif imc >= 35 and imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"


def calcular_IMC():
    nome = input("nome completo do paciente: ")
    altura = float(input("altura: "))
    peso = float(input("peso: "))
    imc = (peso / (altura * altura))

    tipo_imc = validacao_imc(imc)

    print(nome.title() + " o seu ICM é: %.2f" % imc)
    print("Você está " + tipo_imc)

calcular_IMC()
