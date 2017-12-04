#####################################
###########Projecto de Programação 1
#### GRUPO 007
#### Pedro Pereira fc49526
#### Miguel Marôco fc51475
#### Wu Zhen Zé fc51480
#####################################

###AINDA A DECIDIR###
#####################################
########### JOGO -- sim
########### HINT -- sim
########### REGRAS -- sim
#####################################

####ESPAÇO PARA DEFINIR AS FUNÇÕES:::
def existeAs(mao):
    """ Funcao que mostra se tem um As na mao
    Requires: lista da mao
    Ensures: return de um boolean true ou false
    """
    for face in mao:
        if face[0] == 'A':
            existe = True
        else:
            existe = False
    return existe

def valor(mao):
    """ Calcula o valor da mao
    Requires: lista da mao
    Ensures: return do valor dos pontos da mao
    """
    valorCarta = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
                 "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}     #dicionario que contem o valor de cada carta
    soma = 0    #variavel onde se vai acumular o total de pontos de uma mao
    for face in mao:    #ciclo que vai somar os pontos de uma mao
        soma += valorCarta[face[0]]
        if soma > 21 and existeAs(mao) == True: #condicao que decide se o A tem valor 11 ou 1
            soma -= 10
    return soma



###

#Leitura dos dados do jogador
jogador = input("Nome: ")  #Nome
try:
  montante = float(input("Com quantas fichas vais iniciar o jogo?: "))#Dinheiro com que começa o jogo   
except:
  montante = 100.0

try:
  aposta = int(input("Quanto apostas?: "))    #Valor de cada aposta!
except:
  aposta = 10

###COMEÇA O JOGO###
