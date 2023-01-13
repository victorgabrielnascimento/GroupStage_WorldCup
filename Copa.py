import time

####################################################################################################################################MENU

print ("Bem vindo ao simulador de fase de grupos da Copa do Mundo Axon!")
time.sleep(0.3)
print ("             Menu")
time.sleep(0.1)
print ("[1] Simular Fase de Grupos")
time.sleep(0.3)
print ("[2] Visualizar Seleções")
time.sleep(0.2)
print ("[3] Visualizar Regras")
time.sleep(0.2)
print ("[4] Sair da Simulação")
time.sleep(0.2)

opcao = int(input("Digite sua escolha "))

################################################################################################################################FIM MENU

if opcao == 1:
    print ('''              
               
                                                                                                ⠀⠀⠀⣠⣤⣶⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠀⣴⣿⢿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⢐⣿⣿⣿⣟⣤⠈⠉⠉⠉⣿⣿⡟⡦⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠘⡾⣿⣿⣿⣿⡧⢸⠀⠀⣿⣾⢃⡞⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠻⣜⡿⣿⠅⠧⢷⡇⠐⣛⠡⢼⠃⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠀⢿⣿⣶⠜⣿⢹⣜⠐⣼⢴⡟⠀⠀⠀⠀⠀ 
                     Bem amigos da rede Axon, vamos para o                                  ⠀⠀⠀⠀⢸⡿⢻⣿⣆⣿⣮⢴⣽⡿⠁⠀⠀⠀⠀⠀ 
                     ponta pé inicial da fase de grupos!                                    ⠀⠀⠀⠀⠀⢝⢷⣿⣿⣿⡿⠸⣿⠁⠀⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⠏⢻⡏⠀⠀⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠀⠀⠀⢸⣿⣿⠏⣀⣿⡇⠀⠀⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠀⠀⠀⢸⡿⢃⣄⢿⣶⠀⠀⠀⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠀⠀⢀⣜⡵⠂⠀⢠⢿⣧⠀⠀⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠀⠀⣤⡉⠛⠋⠐⠛⠛⣻⣦⠀⠀⠀⠀⠀⠀ 
            Desta vez teremos como país sede o país tropical de Madagascar                   ⠀⠀⠀⠀⠀⠻⠏⠉⣴⠐⡀⠭⠻⢿⡡⠀⠀⠀⠀⠀ 
                                                                                            ⠀⠀⠀⠀⠈⠐⠠⣄⣀⣀⣀⢤⠤⠞⠁⠀

    ''')
    time.sleep(0.2)
    import random

    brgol = (random.randint(6, 8))
    pogol = (random.randint(1, 6))
    jagol = (random.randint(1, 6))
    segol = (random.randint(6, 8))

    pbr = 0
    ppo = 0
    pja = 0
    pse = 0

    vbr = 0
    vpo = 0
    vja = 0
    vse = 0

    ebr = 0
    epo = 0
    eja = 0
    ese = 0 
    
    dbr = 0
    dpo = 0
    dja = 0
    dse = 0

    gmbr = 0
    gmpo = 0
    gmja = 0
    gmse = 0

    gsbr = 0
    gspo = 0
    gsja = 0
    gsse = 0

    sgbr = 0
    sgpo = 0
    sgja = 0
    sgse = 0

    print("          Nesse clima de festa começamos a as partidas, no estádio Moto Moto!")
    time.sleep (0.5)

#################################################################################################################################rodada1

    if brgol > pogol:
        print("\n                                   Brasil {} x {} Polonia       ".format(brgol, pogol))
        pbr += 3
        vbr += 1
        dpo += 1
        gmbr += brgol
        gmpo += pogol
        gsbr += pogol
        gspo += brgol
        print("                              Brasil venceu e fez {} pontos".format(pbr))
        time.sleep(0.2)
    elif brgol == pogol:
        print("                              Empate entre BRASIL E POLONIA {}x{}".format(pbr,ppo))
        pbr += 1
        ppo += 1
        ebr += 1
        epo += 1
        gmbr += brgol
        gmpo += pogol
        gsbr += pogol
        gspo += brgol
    else:
        print("\n                                   Brasil {} x {} Polonia       ".format(brgol, pogol))
        ppo += 3
        vpo += 1
        dbr += 1
        gmbr += brgol
        gmpo += pogol
        gsbr += pogol
        gspo += brgol
        print("                              Polonia venceu e fez {} pontos".format(ppo))
        time.sleep(0.2)

################################################################################################################################Rodada 2

    if brgol > jagol:
        print("\n                                   Brasil {} x {} Japão ".format(brgol, pogol))
        pbr += 3
        vbr += 1
        dja += 1
        gmbr += brgol
        gmja += jagol
        gsbr += jagol
        gsja += brgol
        print("                              Brasil venceu e fez {} pontos".format(pbr))
        time.sleep(0.2)
    elif brgol == jagol:
        print("                              Empate entre BRASIL E JAPAO {}x{}".format(pbr,pja))
        time.sleep(0.2)
        pbr += 1
        pja += 1
        ebr += 1
        eja += 1
        gmbr += brgol
        gmja += jagol
        gsbr += jagol
        gsja += brgol
    else:
        print("\n                                   Brasil {} x {} Japão ".format(brgol, pogol))
        pja += 3
        vja += 1
        dbr += 1
        gmbr += brgol
        gmja += jagol
        gsbr += jagol
        gsja += brgol
        print("                              Japão venceu e fez {} pontos".format(pbr))
        time.sleep(0.2)

################################################################################################################################RODADA 3

    if brgol > segol:
        print("\n                                   Brasil {} x {} Senegal ".format(brgol, segol))
        pbr += 3
        vbr += 1
        dse += 1
        gmbr += brgol
        gmse += segol
        gsbr += segol
        gsse += brgol
        print("                              Brasil venceu e fez {} pontos".format(pbr))
        time.sleep(0.2)
    elif brgol == segol:
        print("                              Empate entre BRASIL E SENEGAL {}x{}".format(pbr,pse))
        pbr += 1
        pse += 1
        ebr += 1
        ese += 1
        gmbr += brgol
        gmse += segol
        gsbr += segol
        gsse += brgol
    else:
        print("\n                                     Brasil {} x {} Senegal ".format(brgol, segol))
        time.sleep(0.2)
        pse += 3
        vse += 1
        dbr += 1
        gmbr += brgol
        gmse += segol
        gsbr += segol
        gsse += brgol
        print("                              Senegal venceu e fez {} pontos".format(pse))
        time.sleep(0.2)

################################################################################################################################RODADA 4

    if pogol > segol:
        print("\n                                     Polonia {} x {} Senegal ".format(pogol, segol))
        time.sleep(0.2)
        ppo += 3
        vpo +=1
        dse +=1
        gmpo += pogol
        gmse += segol
        gspo += segol
        gsse += pogol
        print("                              Polonia venceu e fez {} pontos".format(ppo))
        time.sleep(0.2)
    elif pogol == segol:
        print("\n                              Empate entre POLONIA E SENEGAL {}x{}".format(ppo,pse))
        time.sleep(0.2)
        ppo += 1
        pse += 1
        epo += 1
        ese += 1
        gmpo += pogol
        gmse += segol
        gspo += segol
        gsse += pogol
    else:
        print("\n                                     Polonia {} x {} Senegal ".format(pogol, segol))
        time.sleep(0.2)
        pse += 3
        vse += 1
        dpo += 1
        gmpo += pogol
        gmse += segol
        gspo += segol
        gsse += pogol
        print("                              Senegal venceu e fez {} pontos".format(ppo))
        time.sleep(0.2)

################################################################################################################################RODADA 5

    if pogol > jagol:
        print("\n                                   Polonia {} x {} Japão ".format(pogol, jagol))
        time.sleep(0.2)
        ppo += 3
        vpo += 1
        dja += 1
        gmpo += pogol
        gmja += jagol
        gspo += jagol
        gsja += pogol
        print("                              Polonia venceu e fez {} pontos".format(ppo))
        time.sleep(0.2)
    elif pogol == jagol:
        print("                              Empate entre POLONIA E JAPAO {}x{}".format(ppo,pja))
        time.sleep(0.2)
        ppo += 1
        pja += 1
        epo += 1
        eja += 1
        gmpo += pogol
        gmja += jagol
        gspo += jagol
        gsja += pogol
    else:
        print("\n                                 Polonia {} x {} Japão ".format(pogol, jagol))
        time.sleep(0.2)
        pja += 3
        vja += 1
        dpo += 1
        gmpo += pogol
        gmja += jagol
        gspo += jagol
        gsja += pogol
        print("                              Japão venceu e fez {} pontos".format(pja))
        time.sleep(0.2)

################################################################################################################################RODADA 6 

    if jagol > segol:
        print("\n                                   Japão {} x {} Senegal ".format(jagol, segol))
        time.sleep(0.2)
        pja += 3
        vja += 1
        dse += 1
        gmse += segol
        gmja += jagol
        gsse += jagol
        gsja += segol
        print("                              Japão venceu e fez {} pontos".format(pja))
        time.sleep(0.2)
    elif jagol == segol:
        print("                              Empate entre JAPÃO E SENEGAL {}x{}".format(pja,pse))
        time.sleep(0.2)
        pja += 1
        pse += 1
        eja += 1
        ese += 1
        gmse += segol
        gmja += jagol
        gsse += jagol
        gsja += segol
    else:
        print("\n                                   Japão {} x {} Senegal ".format(jagol, segol))
        time.sleep(0.2)
        pse += 3
        vse += 1
        dja += 1
        gmse += segol
        gmja += jagol
        gsse += jagol
        gsja += segol
        print("                              Senegal venceu e fez {} pontos".format(pse))
        time.sleep(0.2)

#########################################################################################################################FIM DAS RODADAS

    sgbr = gmbr - gsbr
    sgpo = gmpo - gspo
    sgja = gmja - gsja
    sgse = gmse - gsse

    clas = [pbr,ppo,pja,pse]
    pclas = sorted(clas,reverse=True) [:2]

    print ("\n          Fim de papo amigos, vamos ver como ficou as tabelas, começando por:")
    time.sleep(0.4)
    print("\n                 ┌──────────────── • Tabela de Jogos • ──────────────┐")
    time.sleep(0.2)
    print("                                Brasil  [{}] x [{}] Polônia".format(brgol,pogol))
    time.sleep(0.2)
    print("                                Brasil  [{}] x [{}] Japão".format(brgol,jagol))
    time.sleep(0.2)
    print("                                Brasil  [{}] x [{}] Senegal".format(brgol,segol))
    time.sleep(0.2)
    print("                                Polônia [{}] x [{}] Senegal".format(pogol,segol))
    time.sleep(0.2) 
    print("                                Polônia [{}] x [{}] Japão".format(pogol,jagol)) 
    time.sleep(0.2)
    print("                                Japão   [{}] x [{}] Senegal".format(jagol,segol))
    time.sleep(0.2)
    print("                 └───────────────────────────────────────────────────┘")
    time.sleep(0.4)

    print("\nAgora após a tabela de jogos, seguimos para a tabela de classificados, os maiores pontuadores vão as Oitavas de Final!")
    time.sleep(0.4)
    print("                 ┌──────────────────── • Tabela de Pontos • ────────────────┐")
    print("                   Seleções Pontos   V      E     D      GM    GS     SG")
    time.sleep(0.2)
    print("                   Brasil    [{}]    [{}]    [{}]   [{}]    [{}]   [{}]    [{}]".format(pbr,vbr,ebr,dbr,gmbr,gsbr,sgbr)) 
    time.sleep(0.2)
    print("                   Polônia   [{}]    [{}]    [{}]   [{}]    [{}]   [{}]    [{}]".format(ppo,vpo,epo,dpo,gmpo,gspo,sgpo))
    time.sleep(0.2) 
    print("                   Japão     [{}]    [{}]    [{}]   [{}]    [{}]   [{}]    [{}]".format(pja,vja,eja,dja,gmja,gsja,sgja))
    time.sleep(0.2)
    print("                   Senegal   [{}]    [{}]    [{}]   [{}]    [{}]   [{}]    [{}]".format(pse,vse,ese,dse,gmse,gsse,sgse))
    time.sleep(0.2)
    print("                 └──────────────────────────────────────────────────────────┘")
    time.sleep(0.2)

    if pclas[0] == pbr:
        winner1 = "Brasil"
    if pclas[0] == ppo:
        winner1 = "Polônia"
    if pclas[0] == pja:
        winner1 = "Japão"
    if pclas[0] == pse:
        winner1 = "Senagal"


    if pclas[1] == pbr:
        winner2 = "Brasil"
    if pclas[1] == ppo:
        winner2 = "Polônia"
    if pclas[1] == pja:
        winner2 = "Japão"
    if pclas[1] == pse:
        winner2 = "Senagal"
    
    print("\n                       As seleções classificadas foram: {} e {}".format(winner1,winner2))

    exit()

############################################################################################################################FIM OPÇÃO 1

elif opcao == 2:
    print("\n---|Bom te ver torcedor! Aqui você pode ver as escalações da sua seleção favorita!|---\n")

    print ("                         ~~~ |Selecione uma seleção |~~~ ")
    time.sleep(1)
    print ("[1] Brasil")
    time.sleep(0.3)
    print ("[2] Japão")
    time.sleep(0.3)
    print ("[3] Polonia")
    time.sleep(0.3)
    print ("[4] Senegal")
    time.sleep(0.3)
    print ("[5] Voltar")
    time.sleep(0.3)
    
    opcao = int(input("Digite sua escolha "))
    if opcao == 1:
        print('''               ┊                        GOL Alisson                        ┊ 
               ┊                                                           ┊
               ┊            ZAG Marquinhos     ZAG Thiago Silva            ┊
               ┊ LE Alexandro                                   LD Militão ┊
               ┊                                                           ┊
               ┊                       VOL Casemiro                        ┊
               ┊                                                           ┊
               ┊         MA Neymar                     MEI Rodrygo         ┊
               ┊                                                           ┊
               ┊ PE Vini Jr                                     PD Anthony ┊
               ┊                     AT Richarlisson                       ┊
        ''')
        exit()

    if opcao == 2:
        print('''               ┊                         GOL chmidt                             ┊
               ┊                                                                ┊
               ┊               ZAG Yamane           ZAG Taniguchi               ┊
               ┊    LE H. Ito                                      LD Yoshida   ┊
               ┊                                                                ┊
               ┊                       VOL G. Haraguchi                         ┊
               ┊                                                                ┊
               ┊         MEI W. Endo                  MEI D. Kamada             ┊
               ┊                                                                ┊
               ┊  PE R. Doan                                     PD K. Mitoma   ┊
               ┊                     AT T. Asano                                ┊
        ''')
        exit()

    if opcao == 3:
        print('''               ┊                        GOL Grabara                        ┊
               ┊                                                              ┊
               ┊             ZAG Bereszyński      ZAG Glik                    ┊
               ┊  LE Puchacz                                     LD Bednarek  ┊
               ┊                                                              ┊
               ┊                       VOL Klich                              ┊
               ┊                                                              ┊
               ┊         MEI Krychowiak               MEI Góralski            ┊
               ┊                                                              ┊
               ┊  PE Zieliński                                   PD Buksa     ┊
               ┊                     AT Lewandowski                           ┊
        ''')
        exit()

    if opcao == 4:
        print('''                ┊                       GOL E. Mendy                       ┊
                ┊                                                          ┊
                ┊              ZAG Y. Sabaly      ZAG P. Cissé             ┊
                ┊ LE K. Koulibaly                               LD S. Ciss ┊
                ┊                                                          ┊
                ┊                      VOL B. Sarr                         ┊
                ┊                                                          ┊
                ┊   MEI Mendy                                MEI I. Gueye  ┊
                ┊                      B. Dia                              ┊
                ┊                                                          ┊
                ┊            AT Mané              AT I. Sarr               ┊
        ''')
        exit()

    if opcao == 5:
        print("Voltando")
        exit()

elif opcao == 3:
    print('''      ┌───────────────────────────────────────── •🏆• ───────────────────────────────────────────┐
                                ----|Estas são as regras da competição|----                                    

                               |Existem o total de 4 seleções na competição|

                            |Cada uma delas vai jogar uma vez contra as demais|

                     |Se uma seleção ganhar uma partida ela soma o total de +3 pontos|

                     |Se uma seleção empatar uma partida ela soma o total de +1 ponto|

             |Se uma seleção perde uma partida ela não soma nenhum ponto e também não perde|

          |Ao final das partidas averão o total de 2 seleções vão avançar as oitavas de final|

      |Caso algum empate nos pontos seja registrado, o critério de desempate será o Saldo de Gols|
      └────────────────────────────────────────── •⚽️• ──────────────────────────────────────────┘
    ''')
    time.sleep(0.3)
    exit()

elif opcao == 4:
    print(''' 
    
    
                                        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠻⠿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿
                                        ⣿⣿⣿⣿⣿⣿⠟⠉⠄⠄⠄⠄⠄⠄⠄⠉⢟⠉⠄⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿⣿
                                        ⣿⣿⣿⣿⡿⠃⠄⠄⠤⠐⠉⠉⠉⠉⠉⠒⠬⡣⠤⠤⠄⠄⠄⠤⠤⠿⣿⣿⣿⣿
                                        ⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠠⢀⡒⠤⠭⠅⠚⣓⡆⡆⣔⡙⠓⠚⠛⠄⣹⠿⣿
                                        ⣿⠟⠁⡌⠄⠄⠄⢀⠤⠬⠐⣈⠠⡤⠤⠤⣤⠤⢄⡉⢁⣀⣠⣤⣤⣀⣐⡖⢦⣽
                                        ⠏⠄⠄⠄⠄⠄⠄⠄⠐⠄⡿⠛⠯⠍⠭⣉⣉⠉⠍⢀⢀⡀⠉⠉⠉⠒⠒⠂⠄⣻
                                        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠩⠵⠒⠒⠲⢒⡢⡉⠁⢐⡀⠬⠍⠁⢉⣉⣴⣿⣿
    |Obrigado por usar o simulador|     ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⢉⣒⡉⠁⠁⠄⠄⠉⠂⠙⣉⣁⣀⣙⡿⣿⣿
                                        ⠄⠄⠄⠄⠄⠄⠄⠄⢠⠄⡖⢉⠥⢤⠐⢲⠒⢲⠒⢲⠒⠲⡒⠒⡖⢲⠂⠄⢀⣿ 
                                        ⠄⠄⠄⠄⠄⠄⠄⠄⠈⢆⡑⢄⠳⢾⠒⢺⠒⢺⠒⠚⡖⠄⡏⠉⣞⠞⠁⣠⣾⣿ 
                                        ⠄⠄⠄⠄⠄⠄⢆⠄⠄⠄⠈⠢⠉⠢⠍⣘⣒⣚⣒⣚⣒⣒⣉⠡⠤⣔⣾⣿⣿⣿ 
                                        ⠷⣤⠄⣀⠄⠄⠄⠈⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣤⣾⣿⣿⣿⣿⣿ 
                                        ⠄⠄⠉⠐⠢⠭⠄⢀⣒⣒⡒⠄⠄⠄⠄⠄⠄⣀⡠⠶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
                                        ⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠁⠈⠄⠄⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⣿
         
                                                                                                         MADE BY : ~victor gabriel~
    ''')
    exit()