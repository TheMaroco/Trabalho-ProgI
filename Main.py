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
    """ funçao que determina se a mao rebentou ou nao
        Requires : lista da mao
        Ensures: return True no caso de rebentar e False se nao rebentar
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


"""def ronda(i,jogador,aposta):
    ganho = 0
    baralho = ler_baralho(i)
    mao_jogador = [baralho[0],baralho[2]]
    mao_dealer = [baralho[1],baralho[3]]
    valor_jogador = valor(mao_jogador) # pontos do jogador
    valor_dealer = valor(mao_dealer)   # pontos de dealer
    
    ###Joga o jogador:
    if blackjack(mao_jogador):
        resultado_jogador = 'vitória blackjack'
    else:
        
        decisao_jogador = lower(input("HIT, STAND ?"))
        if decisao_jogador != 'hit' or decisao_jogador != 'stand':
            decisao_jogador = 'stand'
        
        while  not bust(mao_jogador) and not blackjack(mao_jogador) and decisao_jogador == 'hit':
            contador = 1
            if lower(input("HIT, STAND ?")) ==  "hit":
                mao_jogador.append(baralho[3+contador])
            contador += 1
            mao_jogador = valor(mao_jogador)   
    
    if blackjack(mao_jogador):
        if blackjack(mao_dealer):
            resultado = 'empate'
        else:
            resultado = 'vitória blackjack'
            ganho = (5 * aposta )/2
    else:


    ###Joga o dealer:
       

"""

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
