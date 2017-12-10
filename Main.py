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
def existem_ases(mao):
    """ Funcao que devolve o numero de ases numa mão
    Requires: lista da mao
    Ensures: return de um int do número de ases na mão
    """
    ases = 0
    for face in mao:
        if face[0] == 'A':
            ases += 1
    return ases

def valor(mao):
    """ Calcula o valor da mao
    Requires: lista da mao
    Ensures: return do valor dos pontos da mao
    """
    
    valorCarta = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
                 "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}     #dicionario que contem o valor de cada carta
    if type(mao) == tuple:
        soma = valorCarta[mao[0]]
    else:
        soma = 0    #variavel onde se vai acumular o total de pontos de uma mao
        for face in mao:    #ciclo que vai somar os pontos de uma mao
            soma += valorCarta[face[0]]
        if soma > 21 and existem_ases(mao) > 1: #condicao que decide se o A tem valor 11 ou 1
            soma = soma - 10*(existem_ases(mao)-1)
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

def calcula_hint(mao_jogador,mao_dealer):
    valor_mao_jogador = valor(mao_jogador)
    
    listaCarta = {}
    listaCarta['A'] = 4
    listaCarta['J'] = 4
    listaCarta['Q'] = 4
    listaCarta['K'] = 4

    for i in range(2,11):              ### criei um dicionario de numeros de cartas que existem no baralho inicial ###
        listaCarta[str(i)] = 4

    contador = 0
    for j in range(contador,len(mao_jogador)):  ### Tirar as cartas da mao do jogador no baralho ###
            for k in mao_jogador[contador][0]:
                    print(k)
                    listaCarta[k] -= 1
            contador += 1
        

    carta_dealer = mao_dealer[0][0]     ### Tirar a carta voltada para cima da mao do dealer no baralho ###
    listaCarta[carta_dealer] -= 1


    rebenta = 0
    nTotalCarta_baralho = 0
    for n in listaCarta:
        nTotalCarta_baralho += listaCarta[n]    ### Calcular quantas vezes que pode rebentar tirando mais uma carta no baralho ###
        if n == 'J' or n =='Q' or n=='K':
            if valor(mao_jogador) + 10 > 21:
                rebenta = rebenta + listaCarta[n]
        elif n == 'A':
            if valor(mao_jogador)+1 > 21:   ### So precisamos ver para caso de A = 1, porque se rebentasse com A = 1, obviamente tambem rebenta com A = 11 
                rebenta += listaCarta[n]
        else:
            if valor(mao_jogador)+int(n) > 21:    
                rebenta += listaCarta[n] 

    prob = round((rebenta / nTotalCarta_baralho),3)  ### Calculo da probabilidade da mao rebentar ###
    return prob


def ronda(i,jogador,aposta):
    ganho = 0
    baralho = ler_baralho(i)
    mao_jogador = [baralho[0],baralho[2]]
    mao_dealer = [baralho[1],baralho[3]]
    valor_jogador = valor(mao_jogador) # pontos do jogador
    valor_dealer = valor(mao_dealer)   # pontos de dealer
    #Print da ronda
    print("\n*** Ronda", i, "***")
    print("Dealer:", mostra_mao(mao_dealer)[:5], "(?,?)")
    print("Jogador:", mostra_mao(mao_jogador), "-", valor_jogador,"-")
    print("\n* Joga", jogador, "*")
    
    ###Joga o jogador:
    if blackjack(mao_jogador):  #Caso de BlackJack na primeira cartada.
        print(jogador, "fez BLACKJACK!")
    else: #Caso de não blackjack na primeira cartada.
        decisao_jogador = (input("HIT, STAND ?")).lower()
        if decisao_jogador != 'hit' and decisao_jogador != 'stand': #Gestão de input inválido
            decisao_jogador = 'stand'

        #PRINT da opção do jogador
        if decisao_jogador == "hit":
            #Loop de jogo
            while  (not bust(mao_jogador)) and (not blackjack(mao_jogador)) and decisao_jogador == "hit": #Em loop Condição testar se pode pedir carta
                 print(jogador, "decidiu HIT")
                 mao_jogador.append(baralho.pop(0)) #Adiciona uma carta à mão do jogador
                 valor_jogador = valor(mao_jogador) #Update dos pontos do jogador
                 print(mostra_mao(mao_jogador), "-", valor_jogador, "-") 
                 if not bust(mao_jogador) and not blackjack(mao_jogador): #De novo, perguntar ao jogador se quer outra carta (só se não BUST ou BJ)
                     decisao_jogador = (input("HIT, STAND ?")).lower()

            if decisao_jogador == "stand": #Print da decisão de jogador
                print(jogador, "decidiu STAND\n")
                
                 
        else: #Jogador decide stand à primeira
            print(jogador, "decidiu STAND\n")  #Print da decisão do jogador


        if bust(mao_jogador):  #Testar se o jogador tem BUST
            ganho = -aposta
            mao_dealer = 21 #Passa o valor 21 para o dealer (que não chega a jogar)
            print("BUST com", valor_jogador, "pontos")
        if blackjack(mao_jogador): #Testar se o jogador tem BlackJack
            print(jogador, "fez BLACKJACK!")

   
     
    ###Testar se vale a pena o dealer jogar:
            
    if valor_jogador == 21:
        if valor(mao_dealer[0]) == 10 or valor(mao_dealer[0]) == 11:
            if blackjack(mao_dealer):
                resultado = "empate"
            else:
                resultado = "vitória Blackjack"
    if not bust(mao_jogador): #Dealer só joga se o jogador não tiver perdido por BUST
        #Dealer Joga:
        print("\n* Joga o dealer *")
        print("Mão dealer:")
        print(mostra_mao(mao_dealer), "-", valor_dealer, "-")
        if blackjack(mao_dealer): #Dealer tem blackjack na primeira cartada
            print("Dealer fez BLACKJACK!")
        else:
        
            if decisao_dealer(mao_dealer) == "HIT": #Dealer decide
                print("Dealer decidiu HIT")
            else:
                print("Dealer decidiu STAND")
            while not blackjack(mao_dealer) and not bust(mao_dealer) and decisao_dealer(mao_dealer) == "HIT": #Em loop Condição testar se pode pedir carta
                mao_dealer.append(baralho.pop(0)) #Dealer recebe carta
                valor_dealer = valor(mao_dealer) #Update dos pontos do dealer
                print(mostra_mao(mao_dealer), "-", valor_dealer, "-") #Print da mão do dealer
                if not bust(mao_dealer) and not blackjack(mao_dealer): #Dealer só decide se não tiver BUST ou BlackJack
                    if decisao_dealer(mao_dealer) == "HIT": #Dealer decide outra vez
                        print("Dealer decidiu HIT")
                    else:
                        print("Dealer decidiu STAND")
            if blackjack(mao_dealer): #Testa se o o dealer tem BlackJakc
                print("Dealer fez BLACKJACK!")
            if bust(mao_dealer): #Testa se o dealer tem BUST
                print("BUST com", valor_dealer, "pontos")
            

    ###TESTAR O RESULTADO DA RONDA

    if valor_jogador > 21 or (valor_jogador<valor_dealer and valor_dealer<=21): #Jogador perde por BUST
        resultado = "derrota"
        ganho = -aposta
    else:
        if valor_dealer > 21: #Jogador ganha por BUST do dealer
            resultado = "vitória"
            ganho = aposta
        elif valor_jogador == valor_dealer:  #Empate
            resultado = "empate"
            ganho = 0
        elif valor_jogador == 21: #Jogador ganha por BlackJack
            resultado = "vitória Blackjack"
            ganho = (3*aposta)/2
        elif valor_jogador > valor_dealer: #Jogador ganha por pontos
            resultado = "vitória"
            ganho = aposta

    return (resultado, ganho)



def jogar():
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

    ##Print do quador inicial###
    print("\n\n=== Vamos começar ===")
    print("Jogador:", jogador)
    print("Saldo inicial:", montante)
    print("Valor da aposta:", aposta)

    #Criação das variáveis estatísticas:
    n_rondas = 1
    montante_inicial = montante
    vitorias = 0
    derrotas = 0
    empates = 0
    v_blackjack = 0
    sair = ""
    #Loop das rondas
    while sair != "quit" and montante != 0:
        resultado = ronda(n_rondas, jogador, aposta)
        print("\nResultado da ronda:", resultado[0], "com ganho", resultado[1])
        montante += resultado[1]
        print("O seu saldo atual é:", montante)
        if resultado[0] == "vitória":
            vitorias += 1
        elif resultado[0] == "vitória Blackjack":
            v_blackjack += 1
        elif resultado [0] == "empate":
            empates += 1
        else:
            derrotas += 1
        n_rondas += 1



        sair = input("Mais uma ronda (QUIT para terminar) ?").lower()

    #Print das estátisticas
    print("\n=== Algumas Estatísticas ===")
    print("\n\n" + jogador, "jogou", n_rondas, "rondas")
    print("Entrou no jogo com", montante_inicial,"e agora tem", montante)
    print("Número de vitórias:", vitorias)
    print("Número de derrotas:", derrotas)
    print("Número de empates:", empates)
    print("Vitórias blackjack:", v_blackjack)

jogar()
    

