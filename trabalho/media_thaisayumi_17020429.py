#Thaís Ayumi - 17020429

def calculo_media() :
    nome = input("nome completo do aluno: ")
    nota1 = float(input("nota do 1º bimestre: "))
    nota2 = float(input("nota do 2º bimestre: "))
    nota3 = float(input("nota do 3º bimestre: "))
    nota4 = float(input("nota do 4º bimestre: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if media >= 6.0:    
        print ("A média final de " + nome.title() + " é %.1f \nAluno aprovado (: " % media )
    else:
        print ("A média final de " + nome.title() + " é %.1f \nAluno reprovado ): " % media )


calculo_media()