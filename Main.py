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
        listBaralho.append(tuple(linha.split()))
      
    baralho.close() #FECHAR O FICHEIRO
    
    return listBaralho    


def mostra_mao(mao):
    """Recebe a lista da mmão e devolve a string formatada dessa mesma mão

    Requires: list da mao
    Ensures: Return da string obtida por formatação da lista
    """
    mao = str(mao)
    mao = mao[1:(len(mao)-1)]
    mao = mao.replace("'", "")
    mao = mao.replace(" ", "")
    mao = mao.replace("),(", ") (")
    return mao

def ronda(i,jogador,aposta):
    ganho = 0
    baralho = ler_baralho(i)
    mao_jogador = [baralho[0],baralho[2]]
    mao_dealer = [baralho[1],baralho[3]]
    valor_jogador = valor(mao_jogador) # pontos do jogador
    valor_dealer = valor(mao_dealer)   # pontos de dealer

    print("*** Ronda", i, "***")
    print("Dealer:", mostra_mao(mao_dealer)[:5], "(?,?)")
    print("Jogador:", mostra_mao(mao_jogador), "-", valor_jogador,"-")
    print("\n* Joga", jogador, "*")
    
    ###Joga o jogador:
    if blackjack(mao_jogador):  #Caso de BlackJack na primeira cartada.
        resultado_jogador = 'vitória blackjack'
        print(jogador, "fez BLACKJACK!")
    else: #Caso de não blackjack na primeira cartada.
        
        decisao_jogador = (input("HIT, STAND ?")).lower()
        print(decisao_jogador)
        if decisao_jogador != 'hit' and decisao_jogador != 'stand': #Gestão de input inválido
            decisao_jogador = 'stand'


        
            
        #PRINT da opção do jogador
        if decisao_jogador == "hit":
            
            while  (not bust(mao_jogador)) and (not blackjack(mao_jogador)) and decisao_jogador == "hit":
                 print(jogador, "decidiu HIT")
                 mao_jogador.append(baralho.pop(0))
                 valor_jogador = valor(mao_jogador)
                 print(mostra_mao(mao_jogador), "-", valor_jogador, "-")
                 if not bust(mao_jogador) and not blackjack(mao_jogador):
                     decisao_jogador = (input("HIT, STAND ?")).lower()

            if decisao_jogador == "stand":
                print(jogador, "decidiu STAND\n")
                resultado_jogador = str(valor_jogador)
                 
        else:
            print(jogador, "decidiu STAND\n")
            resultado_jogador = str(valor_jogador)
     
        
        
       

        if bust(mao_jogador):
            resultado_jogador = "derrota"
            resultado_dealer = "vitória"
            resultado = "derrota"
            ganho = -aposta
            print("BUST com", valor_jogador, "pontos")
        if blackjack(mao_jogador):
            resultado_jogador = "vitória blackjack"
            print(jogador, "fez BLACKJACK!")

   
     
    ###Joga o dealer:
            
    if resultado_jogador == "vitória blackjack":
        if valor(mao_dealer[0]) == 10 or valor(mao_dealer[0]) == 11:
            if blackjack(mao_dealer):
                resultado = "empate"
            else:
                resultado = "vitória blackjack"
                ganho = (5*aposta)/2
    if resultado_jogador != "derrota":
        print("* Joga o dealer *")
        print("Mão dealer:")
        print(mostra_mao(mao_dealer), "-", valor_dealer, "-")
        if blackjack(mao_dealer):
            print("Dealer fez BLACKJACK!")
            resultado_dealer = "vitória blackjack"
        else:
        
            if valor_dealer < 17:
                decisao_dealer = "hit"
                print("Dealer decidiu HIT")
            else:
                decisao_dealer = "stand"
                print("Dealer decidiu STAND")
            while not blackjack(mao_dealer) and not bust(mao_dealer) and decisao_dealer == "hit":
                mao_dealer.append(baralho.pop(0))
                valor_dealer = valor(mao_dealer)
                print(mostra_mao(mao_dealer), "-", valor_dealer, "-")
                if valor_dealer < 17:
                    decisao_dealer = "hit"
                    print("Dealer decidiu HIT")
                else:
                    decisao_dealer = "stand"
                    print("Dealer decidiu STAND")
            resultado_dealer = str(valor_dealer)
            if blackjack(mao_dealer):
                print("Dealer fez BLACKJACK!")
                resultado_dealer = "vitória blackjack"
            if bust(mao_dealer):
                resultado_dealer = "BUST"
                print("BUST com", valor_dealer, "pontos")
            

    ###TESTAR O RESULTADO DA RONDA

    if resultado_jogador == "vitória blackjack" and resultado_dealer == "vitória blackjack": # Empatam os dois com blackjack
        resultado = "empate"
        ganho = 0
    elif resultado_dealer == "BUST": #Dealer perde por BUST
        resultado = "vitória"
        ganho = aposta
    elif resultado_dealer < resultado_jogador: #Dealer perde por pontos
        resultado = "vitória"
        ganho = aposta
    elif resultado_dealer > resultado_jogador: #Dealer ganha por pontos
        resultado = "derrota"
        ganho = -aposta
    else:
        resultado = "empate" #Empatam por pontos


    return (resultado, ganho)




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

regra = input("Qual a regra do casino (s17 ou h17)?: ").upper() #Regra do casino
if regra != "H17":
    regra = "S17"

###COMEÇA O JOGO###
