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
    
    ases = 0
    for face in mao:
        if face[0] == 'A':
            ases += 1
    return ases

def valor(mao):
    """Calcula o valor de uma mão.
    Por exemplo, dada a seguinte mão:
        [("5", "P"), ("K", "C")]
    A função deve devolver o inteiro 15.

    Requires: Uma mão (lista de pares de strings (face, naipe))
    Ensures: Um inteiro com o valor total da mão
    """
    pass

    valorCarta = {"A":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7,  
                 "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}     #dicionario que contem o valor de cada carta
    if type(mao) == tuple:
        soma = valorCarta[mao[0]]
    else:
        soma = 0    #variavel onde se vai acumular o total de pontos de uma mao
        for face in mao:    #ciclo que vai somar os pontos de uma mao
            soma += valorCarta[face[0]]
        n_ases = existem_ases(mao)
        while soma > 21 and n_ases >= 1: #condicao que decide se o A tem valor 11 ou 1
            soma = soma - 10
            n_ases -= 1
    return soma

def soft(mao):
    """Verifica se uma mão é 'soft' ou 'hard', ou seja, se a adição de mais uma
    carta à mão nunca fará o jogador 'rebentar'.
    Por exemplo, dada a seguinte mão:
        [("A", "P"), ("6", "C")]
    A função deve devolver o valor True.

    Requires: mao: uma mão (lista de pares de strings (face, naipe))
    Ensures: um Booleano (True ou False). True se a adição de uma carta à mão
    nunca possa fazer o seu valor ultrapassar os 21 pontos (mão 'soft'). False
    False caso a adição de uma carta à mão a possa fazer ultrapassar os 21
    pontos (mão 'hard').
    """
    pass

    mao_sem_ases = [carta for carta in mao if carta[0] != 'A'] #Lista das cartas da mão que não são ases.

    if existem_ases(mao) > 0 and (valor(mao_sem_ases) + (existem_ases(mao) - 1)) <= 10:
        soft = True 
    else:
        soft = False                             
    return soft

def decisao_dealer(mao, regra):
    """Calcula a decisão do dealer para a uma dada mão.
    Por exemplo, dada a seguinte mão:
        [("10", "P"), ("2", "E")]
    A função deve devolver o valor "HIT".

    Requires: Uma mão (lista de pares de strings (face, naipe))
    Ensures: uma de duas strings ("HIT" ou "STAND"), consoante o valor da
    mão e as regras do casino.
    """
    pass
    
    pontos_dealer = valor(mao)
    
    decisao = "STAND"
    
    
    if pontos_dealer < 17:         
        decisao = 'HIT'
    elif pontos_dealer == 17:
        if regra == "H17":
            if soft(mao):
                decisao = "HIT"
        
    return decisao
def bust(mao):
    """Verifica se uma mão 'rebenta', ou seja, se o valor da mão
    ultrapassa os 21 pontos.
    Por exemplo, dada a seguinte mão:
        [("10", "P"), ("K", "C"), ("2", "E")]
    A função deve devolver o valor True.

    Requires: mao: uma mão (lista de pares de strings (face, naipe))
    Ensures: um Booleano (True ou False), consoante o valor da mão
    ultrapassa ou não os 21 pontos
    """
    pass
     
    rebentou = False
    if valor(mao) > 21:
        rebentou = True
    return rebentou

def blackjack(mao):
    """Verifica se uma mão representa um blackjack, ou seja, se contém
    exactamente um ás e uma carta de valor 10.
    Por exemplo, dada a seguinte mão:
        [("A", "P"), ("10", "C")]
    A função deve devolver o valor True.

    Requires: mao: uma mão (lista de pares de strings (face, naipe))
    Ensures: um Booleano (True ou False), consoante a mão contém
    ou não um ás e uma carta de valor 10.
    """
    pass
    
    Blackjack = False
    if valor(mao) == 21 :
        Blackjack = True

    return Blackjack
     
def ler_baralho(n):
    """Lê um baralho do ficheiro com o número específicado
    como parâmetro e devolve o baralho contido neste.
    Por exemplo dado 10 como argumento a função deve ler o ficheiro
    de nome "baralho_10.txt".

    Requires: n: um inteiro positivo n, que representa o número do
    baralho a ler.
    Ensures: O baralho contido no ficheiro, como uma lista de
    pares de strings (face, naipe)
    """
    pass
    
    strBaralho = "baralho_" + str(n) + ".txt" #ARTIMANHA PARA LER OS BARALHOS INDICE n

    baralho = open(strBaralho, 'r') #ABRE O BARALHO
    listBaralho = [] #Lista do baralho
    for linha in baralho:
        listBaralho.append(tuple(linha.split()))
      
    baralho.close() #FECHAR O FICHEIRO
    
    return listBaralho    


def mostra_mao(mao):
    """Recebe a lista das cartas de uma mão
    e devolve uma string das cartas dessa mão de acordo com acordo
    tipologia específicada. 
    Por Exemplo, dada a lista:
        [('A', 'E'),('A','C')]
    devolve a string:
        (A,E)(A,C)
    
    Requires: mao: uma lista com os tuplos que representam as cartas
    de um mão.
    Ensures: uma string com a tipologia específica do jogo.
    """
    
    mao = str(mao)
    mao = mao[1:(len(mao)-1)]
    mao = mao.replace("'", "")
    mao = mao.replace(" ", "")
    mao = mao.replace("),(", ") (")
    return mao

def calcula_hint(mao_jogador,mao_dealer):
    """Calcula a probabilidade de o jogador rebentar se fizer "HIT" sobre a mão
    dada, com base nas cartas que estão visíveis (as suas e as cartas visíveis da
    mão do dealer).

    Requires: mao_jogador: a mão do jogador (lista de pares de strings (face, naipe)), e
    mao_dealer: a mão do dealer (lista de pares de strings (face, naipe))
    Ensures: um float representando a probabilidade de o jogado rebentar se
    fizer "HIT", dadas as cartas em jogo, arredondado à terceira casa decimal
    """
    pass
    
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


def ronda(i,jogador,aposta,regra):
    """Executa uma ronda completa, para o jogador dado. Esta função produz ainda
    toda a interação com o utilizador relativa à ronda i (de acordo com o
    ilustrado nos exemplos anexos ao enunciado)

    Requires: i: inteiro positivo, que representa o número da ronda;
    jogador: uma string com o nome do jogador; aposta: inteiro com o valor da
    aposta.
    Ensures: um par (resultado, ganho), onde resultado é uma string
    de entre "vitória blackjack", "vitória", "derrota" ou "empate", e ganho
    é um float, positivo ou negativo, arredondado a duas casas decimais,
    correspondente ao valor que o jogador ganhou ou perdeu nessa ronda.
    """
    pass
    
    ganho = 0
    baralho = ler_baralho(i)
    mao_jogador = [baralho.pop(0),baralho.pop(1)]
    mao_dealer = [baralho.pop(0),baralho.pop(0)]
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
        decisao_jogador = (input("HIT, STAND ou HINT? ")).lower()
        if decisao_jogador != 'hit' and decisao_jogador != 'stand' and decisao_jogador != 'hint': #Gestão de input inválido
            decisao_jogador = 'stand'

        #PRINT da opção do jogador
        if decisao_jogador == "hit" or decisao_jogador == "hint": #jogador decide hit
            #Loop de jogo
            while  (not bust(mao_jogador)) and (not blackjack(mao_jogador)) and decisao_jogador == "hit" or decisao_jogador == "hint":
                #Em loop Condição testar se pode pedir carta
                #Testa se o jogador decidiu HIT ou Hint
                if decisao_jogador == "hit":
                     print(jogador, "decidiu HIT")
                     mao_jogador.append(baralho.pop(0)) #Adiciona uma carta à mão do jogador
                     valor_jogador = valor(mao_jogador) #Update dos pontos do jogador
                     print(mostra_mao(mao_jogador), "-", valor_jogador, "-") 
                     if not bust(mao_jogador) and not blackjack(mao_jogador): #De novo, perguntar ao jogador se quer outra carta (só se não BUST ou BJ)
                         decisao_jogador = (input("HIT, STAND ou HINT? ")).lower() 
                else:
                    print(jogador, "decidiu HINT")
                    print("A probabilidade de rebentar com a próxima carta é:", calcula_hint(mao_jogador,mao_dealer))
                    decisao_jogador = (input("HIT, STAND ou HINT? ")).lower() #Reavalia a decisão do jogador
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
                print("Mão dealer:", mostra_mao(mao_dealer))
                print("Dealer fez BLACKJACK!")
                resultado = "empate"
            else:
                resultado = "vitória Blackjack"

    
    
    if not bust(mao_jogador) and not blackjack(mao_jogador): #Dealer só joga se o jogador não tiver perdido por BUST
        #Dealer Joga:
        print("* Joga o dealer *")
        print("Mão dealer:")
        print(mostra_mao(mao_dealer), "-", valor_dealer, "-")
        if blackjack(mao_dealer): #Dealer tem blackjack na primeira cartada
            print("Dealer fez BLACKJACK!")
        else:
        
            if decisao_dealer(mao_dealer, regra) == "HIT": #Dealer decide
                print("Dealer decidiu HIT")
            else:
                print("Dealer decidiu STAND")
            while not blackjack(mao_dealer) and not bust(mao_dealer) and decisao_dealer(mao_dealer, regra) == "HIT": #Em loop Condição testar se pode pedir carta
                mao_dealer.append(baralho.pop(0)) #Dealer recebe carta
                valor_dealer = valor(mao_dealer) #Update dos pontos do dealer
                print(mostra_mao(mao_dealer), "-", valor_dealer, "-") #Print da mão do dealer
                if not bust(mao_dealer) and not blackjack(mao_dealer): #Dealer só decide se não tiver BUST ou BlackJack
                    if decisao_dealer(mao_dealer, regra) == "HIT": #Dealer decide outra vez
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
    """Joga um jogo completo, com um número variável de rondas.
    Esta função produz toda a  interação com o utilizador (de acordo com o
    ilustrado nos exemplos anexos ao enunciado).

    Requires: a função não recebe argumentos
    Ensures: a função não devolve nenhum valor.
    """
    pass

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
    while sair != "quit" and montante != 0 and montante >= aposta:
        resultado = ronda(n_rondas, jogador, aposta, regra)
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



        sair = input("Mais uma ronda (QUIT para terminar)?").lower()

    #Print das estátisticas
    print("\n=== Algumas Estatísticas ===")
    print("\n\n" + jogador, "jogou", n_rondas-1, "rondas")
    print("Entrou no jogo com", montante_inicial,"e agora tem", montante)
    print("Número de vitórias:", vitorias + v_blackjack)
    print("Número de derrotas:", derrotas)
    print("Número de empates:", empates)
    print("Vitórias blackjack:", v_blackjack)

jogar()
    

        
