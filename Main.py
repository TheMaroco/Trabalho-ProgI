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

def decisao_dealer(mao):
    """ Determinar a decisão do dealer
        Require : lista da mão do dealer
        Ensures Return HIT ou STAND
    """
    pontos_dealer = valor(mao)

    if pontos_dealer < 17 :
        return 'HIT'
    else:
        return 'STAND'

def bust(mao):
    """ funçao que determina se o mao rebentou ou nao
        Requires : lista da mao
        Ensures: return True no caso de rebentar e False nao rebentar
    """
    
    rebentou = False
    if valor(mao) > 21:
        rebentou = True
    return rebentou

def blackjack(mao):
    """ Verificar se tem balckjack na mão
        Requires : lista da mão inicial
        Ensures: se der 21 pontos devolve True, caso contrario devolve False
    """
    Blackjack = False
    if valor(mao) == 21 :
        Blackjack = True

    return Blackjack
     
    
def ler_baralho(n):
    """Lê o baralho usado na ronda n

    Requires: int com número da ronda
    Ensures: Lista com o Baralho respetivo à ronda
    """
    strBaralho = "baralho_" + str(n) + ".txt" #ARTIMANHA PARA LER OS BARALHOS INDICE n

    baralho = open(strBaralho, 'r') #ABRE O BARALHO
    listBaralho = [] #Lista do baralho
    for linha in baralho:
        listBaralho.append(baralho.readline()[:-1].split()) #GOD MODE DE MODULOS PARA criar o baralho
    baralho.close() #FECHAR O FICHEIRO
    
    return listBaralho

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
