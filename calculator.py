def soma(numero1,numero2):
    resultado=numero1+numero2
    print (resultado)
    outra_Operacao()

def subtracao(numero1,numero2):
    resultado=numero1-numero2
    print (resultado)
    outra_Operacao()

def divisao(numero1,numero2):
    resultado=numero1/numero2
    print (resultado)
    outra_Operacao()

def multiplicacao(numero1,numero2):
    resultado=numero1*numero2
    print (resultado)
    outra_Operacao()

def entrada():
    numero1 = input("Digite o primeiro numero: ")
    numero2 = input("Digite o segundo numero: ")
    numero1=float(numero1)
    numero2=float(numero2)
    escolhas()

def outra_Operacao():
    print ("Quer fazer outra operação?")
    print ("1 para Sim")
    print ("2 para Não")
    escolha2=input()
    escolha2=int(escolha2)
    if escolha2==1:
        entrada()
    else:
        print("Obrigado por usar essa calculadora!!!")

def escolhas():
    print("Qual operação você quer realizar?")
    print("Digite 1 para soma ")
    print("Digite 2 para subtração ")
    print("Digite 3 para divisão ")
    print("Digite 4 para multiplicação ")
    escolha=input()
    escolha=int(escolha)
    if escolha == 1:
        print("Você escolheu soma")
        soma()      
    if escolha == 2:
        subtracao()
    if escolha == 3:
        divisao()
    if escolha == 4:
        multiplicacao()

entrada()
