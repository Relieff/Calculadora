from math import sqrt
from time import sleep
coresbg = {'branco':'\033[107m', #Não é o ideal, mas como não encotrei uma maneira melhor vai essa "biblioteca" mesmo
            'vermelho':'\033[41m',
            'verde':'\033[42m,',
            'amarelo':'\033[43m',
            'azul':'\033[44m',
            'magenta':'\033[45m',
            'ciano':'\033[46m',
            'limpa':'\033[m',
            'cinza':'\033[47m'}
coresletras = {'limpa':'\033[m',
               'azul':'\033[34m',
               'amarelo':'\033[33m',
               'vermelho':'\333[31m',
               'pretoebranco':'\033[7;30m'}

def soma(x,y):  #Def() para definir uma função
    return x + y #Return para chamar a função
def subtracao (x,y):
    return x - y
def multp (x,y):
    return x * y
def divsao (x,y):
    return x / y
def potencia (x,y):
    return x ** y
def raiz_quadrada (x):
    return sqrt(x)

def calculadora():
    while True:

        print ('=' *50)
        titulo = 'Calculadora Simples'
        print(titulo.center(50)) #Preciso de chamar o numero de caracteres para o center() funcionar
        print ('=' *50)


        print('faça uma escolha:')
        print('1 - soma')
        print('2 - subtração')
        print('3 - multiplicação')
        print('4 - divisão')
        print('5 - potência')
        print('6 - raiz quadrada')

        escolha = int(input('Escolhas disponíveis: \n --> [1] \n --> [2] \n --> [3] \n --> [4] \n --> [5] \n --> [6] \n ===> Digite sua escolha: '))
        sleep(0.3)

        while escolha not in [1,2,3,4,5,6]:
            sleep(0.3)
            print('Opção inválida, tente novamente')
            sleep(0.5)
            escolha = float(input('Escolhas disponíveis: \n --> [1] \n --> [2] \n --> [3] \n --> [4] \n --> [5] \n --> [6] \n ===> Digite sua escolha: '))

        if escolha in [1,2,3,4,5]:
            num1 = float(input('Digite um número: '))
            num2 = float(input('Digite outro número: '))
            if escolha == 1:
                print(f'A soma entre {num1} e {num2} é --->',coresbg['amarelo'], soma(num1,num2), coresbg['limpa'])
            elif escolha == 2:
                print(f'A subtração entre {num1} e {num2} é --->',coresbg['amarelo'], subtracao(num1,num2), coresbg['limpa'])
            elif escolha == 3:
                print(f'A multiplicação entre {num1} e {num2} é --->',coresbg['amarelo'], multp(num1,num2), coresbg['limpa'])
            elif escolha == 4:
                print(f'A divisão entre entre {num1} e {num2} é --->',coresbg['amarelo'], divsao(num1,num2), coresbg['limpa'])
            elif escolha == 5:
                print(f'O resultado da potência envolvendo o número {num1} e {num2} é --->',coresbg['amarelo'], potencia(num1,num2),coresbg['limpa'])

        if escolha == 6:
            num1 = float(input('Digite um número: '))
            print(f'O resultado da raiz quadrada de {num1} é --->', coresbg['amarelo'], raiz_quadrada(num1), coresbg['limpa']) #abrir a biblioteca e lembrar de fechar ela pra ficar limitada a um lugar
        pergunta = str(input('Deseja fazer outra operação? \n [S]sim \n [N]não \n ===> ')).strip().upper()
        if pergunta == 'N':
            print('Encerrando programa.')
            break
        elif pergunta != 'S':
            print('Resposta inválida. Encerrando programa')
calculadora()
    


