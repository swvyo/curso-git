# Início do programa!
print ("")
print('HELPIC v1.0' .center(100))
print ("")
print(" Bem-vindo(a) a versão 1.0 do Helpic, um guia simples para iniciantes em fotografia.".center(100))
print ("")
usu=(input(" Digite o seu nome para começar: "))# Aqui receberá o nome do usúario que será utilizado até o fim do programa!
print ("")
print("▲ ainda não são aceitos caracteres to tipo letras ou strings, utilize apenas números ▲ \n" .center(100))

#padronização das pontuaçoes :
# A partir daqui será impresso o menu do programa!
print("Escolha uma das opções abaixo para começar")
print("")

# Opção escolhida irá gerar as opções alternativas e subsequentes!
import webbrowser
opcao = 1
while True: # Repetição, para que o app entre em loop!

    arquivo = open("menup.txt", "r")
    print(arquivo.read())
    arquivo.close()
    print("--------------------------------------------")
    print("Caso queira encerrar o app, digite 9")
    print("")
    opcao = int(input("Insira a opção do MENU PRINCIPAL desejada: "))
    if opcao == 9:
        print('Obrigado por utilizar o nosso programa! Até mais...')
        break
    elif opcao == 1:
        print("")
        print("~~~~~~~~ INICIANTE ~~~~~~~~".center(130))
        print('''
        Para começarmos, informe o seu conhecimento em fotografia:
        
        Digite 1, se você não conhece muito esta aréa e quer iniciar agora mesmo!
        Digite 2, se você conhece a aréa e quer conhecer formas de como divulgar seu trabalho!
        Digite 3, para saber como organizar bem seu portifólio de iniciante!
        Qualquer outro número para retornar ao menu, ou 0 para fechar o programa.

''')
        opc1 = (int(input("Digite a sua escolha: ")))
        print ("--------------------------------------------")
        if opc1 == 0:
            print ('Obrigado por utilizar o nosso programa! Até mais...')
            break
        elif opc1 == 1:
            webbrowser.open('https://i.imgur.com/Jy5w1yf.png')
            print("--------------------------------------------")
        elif opc1 == 2:
            webbrowser.open('https://i.imgur.com/PkeWQoF.png')
            print("--------------------------------------------")
        elif opc1 == 3:
            webbrowser.open('https://i.imgur.com/nGet1ZF.png')
            print("--------------------------------------------")
        else:
            print("--------------------------------------------")
    elif opcao == 2:
        print("")
        print("~~~~~~~~ FOTOGRAFIA MOBILE ~~~~~~~~" .center(130))
        print("")
        webbrowser.open('https://www.wefashiontrends.com/como-fotografar-com-o-celular-confira-dicas-de-fotografia-mobile/')
        print("--------------------------------------------")
    elif opcao == 3:
        print("")
        print("~~~~~~~~ CÂMERAS ~~~~~~~~" .center(130))
        print('''
        Chegou a hora de fazer aquele orçamento!
        Antes de comprar um bom equipamento é sempre bom pesquisar.
        Vamos te auxiliar nisso, chill!
        Para prosseguir, escolha qual tipo de câmera você procura.''')
        print("--------------------------------------------")
        print("        Para Compactas, digite 1")
        print("        Para DSLR's, digite 2")
        print("        Para Semiprofissionais, digite 3")
        print("--------------------------------------------")
        print("")
        typoCam = int(input("Digite a sua escolha: "))
        if typoCam == 1:
            print("")
            print("~~~~~~~~ COMPACTAS! ~~~~~~~~" .center(130))
            print("")
            print(" ▲ Os preços podem variar de acordo com a loja e a procura pelo produto ▲  \n")
            print('''  Estas são algumas opções para você, para abrir-las basta digitar o número correspondente.
                        Caso queira voltar ao menu, utilize qualquer outro número.''')
            print("=======================================")
            print("        1. Samsung PL120")
            print("        2. Sony Cyber-shot Dsc-w800")
            print("        3. Sony Hd Zoom 8 X")
            print("        4. Sony Cyber-shot DSC-W830")
            print("        5. Sony Cybershot Dsc-w530")
            print("=======================================")
            print("        6. Sony Cyber-shot DSC-W830")
            print("        7. Canon Powershot Elph 300 Hs")
            print("        8. Nikon A300")
            print("=======================================")
            abrir = int(input("Insira a sua opção: "))
            if abrir == 1:
                webbrowser.open('https://goo.gl/qpXYoY')
                print("--------------------------------------------")
            elif abrir == 2:
                webbrowser.open('https://goo.gl/jSQxzA')
                print("--------------------------------------------")
            elif abrir == 3:
                webbrowser.open('https://goo.gl/JxizRp')
                print("--------------------------------------------")
            elif abrir == 4:
                webbrowser.open('https://goo.gl/3iNHfP')
                print("--------------------------------------------")
            elif abrir == 5:
                webbrowser.open('https://goo.gl/Bgt3Rg')
                print("--------------------------------------------")
            elif abrir == 6:
                webbrowser.open('https://goo.gl/qQFFwV')
                print("--------------------------------------------")
            elif abrir == 7:
                webbrowser.open('https://goo.gl/nsVe1E')
                print("--------------------------------------------")
            elif abrir == 8:
                webbrowser.open('https://goo.gl/ijLEKk')
                print("--------------------------------------------")
            else:
                print("--------------------------------------------")
        elif typoCam == 2:
            print("DSLR!, equipamentos deste porte custam mais que 1000!.")
            print("    \n        ▲ Os preços podem variar de acordo com a loja e a procura pelo produto ▲  \n")
            print('''  Estas são algumas opções para você, para abrir-las basta digitar o número correspondente.
                        Caso queira voltar ao menu, utilize qualquer outro número.''')
            print("=======================================")
            print("         1. Nikon Coolpix L340, (para saber mais: https://goo.gl/9wPfxs)")
            print("         2. Nikon Coolpix B500, (para saber mais: https://goo.gl/fbx4DF)")
            print("         3. Nikon DSLR-D3300, (para saber mais: https://goo.gl/A97nuz)")
            print("         4. Canon PowerShot SX400, (para saber mais: https://goo.gl/suFg57")
            print("=======================================")
            abrir = int(input("Insira sua opção: "))
            if abrir == 1:
                webbrowser.open('https://goo.gl/9wPfxs')
                print("--------------------------------------------")
            elif abrir == 2:
                webbrowser.open('https://goo.gl/fbx4DF')
                print("--------------------------------------------")
            elif abrir == 3:
                webbrowser.open('https://goo.gl/A97nuz')
                print("--------------------------------------------")
            elif abrir == 4:
                webbrowser.open('https://goo.gl/suFg57')
                print("--------------------------------------------")
            else:
                print("--------------------------------------------")
        elif typoCam == 3:
            print("  SEMIPROFISSIONAIS! Equipamentos deste porte custam bem mais que as DSLR's normais!.")
            print("    \n        ▲ Os preços podem variar de acordo com a loja e a procura pelo produto ▲  \n")
            print('''  Estas são algumas opções para você, para abrir-las basta digitar o número correspondente.
                        Caso queira voltar ao menu, utilize qualquer outro número.''')
            print("=======================================")
            print("        1. Canon Powershot Sx530hs")
            print("        2. Canon PowerShot SX720HS")
            print("        3. Nikon Coolpix P900")
            print("        4. Sony Cyber-shot DSC-HX400V")
            print("=======================================")
            abrir = int(input("Insira sua opção: "))
            if abrir == 1:
                webbrowser.open('https://goo.gl/pXi4sP')
                print("--------------------------------------------")
            elif abrir == 2:
                webbrowser.open('https://goo.gl/Tq1aK4')
                print("--------------------------------------------")
            elif abrir == 3:
                webbrowser.open('https://goo.gl/duxYuc')
                print("--------------------------------------------")
            elif abrir == 4:
                webbrowser.open('https://goo.gl/Wj3i6Q')
                print("--------------------------------------------")
            else:
                print("--------------------------------------------")
    elif opcao == 4:
        print("")
        print("~~~~~~~~ APLICATIVOS MOBILE ~~~~~~~~" .center(130))
        print("")
        print("  {}, existem milhares de aplicativos movéis que podem te ajudar a fotografar.".format(usu))
        print("  São desde emuladores de câmeras antigas até tratamento profissional fotográfico.")
        print("  Estes aplicativos estão disponíveis para, principalmente, Android e IOS. \n")
        print("--------------------------------------------")
        print("        Se você utiliza um dispositivo Android, digite 1")
        print("        Ou se utiliza um dispositivo IOS, digite 2 \n")
        print("Digite qualquer número para voltar ao menu principal.")
        print("--------------------------------------------")
        sisT = int(input("Digite a opção referente ao seu sistema operacional: "))
        if sisT == 1:
            print("")
            print("  ANDROID... Humm. Vamos lá, descobrir alguns apps para o seu robôzinho verde!")
            print("  {}, diante da infinidade de aplicativos, organizamos uma seleção para você!.".format(usu))
            print("  Então {}, qual é o tipo de aplicativo que você está procurando?.".format(usu))
            print("--------------------------------------------")
            print("        Para aplicativos de edição básica, digite 1")
            print("        Para aplicativos de edição profissional, digite 2 \n")
            print("Digite qualquer outro número para voltar ao menu principal") ###### CORRETO???
            print("--------------------------------------------")
            apps = int(input("Insira a sua opção: "))
            if apps == 1:
                print("")
                print("  Aqui estão alguns aplicativos para edição básica de fotos... ")
                print("")
                print(" ▲Para ser redirecionado para a página de download, digite a opção referente ao aplicativo▲")
                print("")
                print("Digite qualquer outro número para voltar ao menu principal") #CORRETO???????
                print("--------------------------------------------")
                print("        1. Fotor")
                print("        2. AirBrush")
                print("        3. MIX by Camera360")
                print("        4. Adobe Photoshop Express")
                print("--------------------------------------------")
                print("")
                appso = int(input("Insira a sua opção: "))
                if appso == 1:
                    webbrowser.open('https://goo.gl/H6NRXn')
                    print("--------------------------------------------")
                elif appso == 2:
                    webbrowser.open('https://goo.gl/CbSCRW')
                    print("--------------------------------------------")
                elif appso == 3:
                    webbrowser.open('https://goo.gl/mRkjBH')
                    print("--------------------------------------------")
                elif appso == 4:
                    webbrowser.open('https://goo.gl/YUArpz')
                    print("--------------------------------------------")
                else:
                    print("--------------------------------------------")
            if apps == 2:
                print("")
                print("  Aqui estão alguns aplicativos para edição profissional de fotos...")
                print("")
                print(" ▲Para ser redirecionado para a página de download, digite a opção referente ao aplicativo▲")
                print("")
                print("Digite qualquer outro número para voltar ao menu principal")
                print("--------------------------------------------")
                print("        1. Adobe Photoshop Lightroom CC")
                print("        2. VSCO")
                print("        3. Snapseed")
                print("        4. Afterlight")
                print("        5. Polarr")
                print("        6. PicsArt Photo Studio")
                print("--------------------------------------------")
                print("")
                apsso1 = int(input("Insira a sua opção: "))
                if apsso1 == 1:
                    webbrowser.open('https://goo.gl/wghUqh')
                    print("--------------------------------------------")
                elif apsso1 == 2:
                    webbrowser.open('https://goo.gl/LgwU8K')
                    print("--------------------------------------------")
                elif apsso1 == 3:
                    webbrowser.open('https://goo.gl/eDtY2S')
                    print("--------------------------------------------")
                elif apsso1 == 4:
                    webbrowser.open('https://goo.gl/31EwVy')
                    print("--------------------------------------------")
                elif apsso1 == 5:
                    webbrowser.open('https://goo.gl/PNKXYe')
                    print("--------------------------------------------")
                elif apsso1 == 6:
                    webbrowser.open('https://goo.gl/3vJxTn')
                    print("--------------------------------------------")
                else:
                    print("--------------------------------------------")
        elif sisT == 2:
            print("")
            print("  IOS, wow! Preparado para descobrir alguns apps para alimentar a sua maçã?")
            print("  {}, diante uma infinidade de aplicativos, organizamos uma seleção para você!.".format(usu))
            print("  Então {}, qual seria o tipo de aplicativo que você estaria procurando?.".format(usu))
            print("--------------------------------------------")
            print("       Para aplicatvos de edição básica, digite 1")
            print("       Para aplicativos de edição profissional, digite 2 \n")
            print("Digite qualquer outro número para voltar ao menu principal")
            print("--------------------------------------------")
            print("")
            apps = int(input("Insira a sua opção: "))
            if apps == 1:
                print("")
                print("  Aqui estão alguns aplicativos para edição básica de fotos...")
                print("")
                print(" ▲Para ser redirecionado para a página de download, digite a opção referente ao aplicativo▲")
                print("")
                print("Digite qualquer outro número para voltar ao menu principal")
                print("--------------------------------------------")
                print("        1. Fotor")
                print("        2. AirBrush")
                print("        3. MIX by Camera360")
                print("        4. Adobe Photoshop Express")
                print("--------------------------------------------")
                print("")
                appso = int(input("Insira a sua opção: "))
                if appso == 1:
                    webbrowser.open('https://goo.gl/hwQw4u')
                    print("--------------------------------------------")
                elif appso == 2:
                    webbrowser.open('https://goo.gl/W5MsLn')
                    print("--------------------------------------------")
                elif appso == 3:
                    webbrowser.open('https://goo.gl/byvWqb')
                    print("--------------------------------------------")
                elif appso == 4:
                    webbrowser.open('https://goo.gl/zh4UPz')
                    print("--------------------------------------------")
                else:
                    print("--------------------------------------------")
                    
            if apps == 2:
                print("")
                print("  Aqui estão alguns aplicativos para edição profissional de fotos...")
                print("")
                print(" ▲Para ser redirecionado para a página de download, digite a opção referente ao aplicativo▲")
                print("")
                print("Digite qualquer outro número para voltar ao menu principal")
                print("--------------------------------------------")
                print("        1. Adobe Photoshop Lightroom CC")
                print("        2. VSCO")
                print("        3. Snapseed")
                print("        4. Afterlight")
                print("        5. Polarr")
                print("        6. PicsArt Photo Studio")
                print("--------------------------------------------")
                print("")
                apsso1 = int(input("Insira a sua opção: "))
                if apsso1 == 1:
                    webbrowser.open('https://goo.gl/992f6q')
                    print("--------------------------------------------")
                elif apsso1 == 2:
                    webbrowser.open('https://goo.gl/23Da4V')
                    print("--------------------------------------------")
                elif apsso1 == 3:
                    webbrowser.open('https://goo.gl/sT7KSS')
                    print("--------------------------------------------")
                elif apsso1 == 4:
                    webbrowser.open('https://goo.gl/Rgwn3C')
                    print("--------------------------------------------")
                elif apsso1 == 5:
                    webbrowser.open('https://goo.gl/JjPXa6')
                    print("--------------------------------------------")
                elif apsso1 == 6:
                    webbrowser.open('https://goo.gl/nXSCoF')
                    print("--------------------------------------------")
                else:
                    print("--------------------------------------------")                
    elif opcao == 5:
        print("")
        print ("~~~~~~ CORES E ORGANIZAÇÕES ~~~~~~" .center(130))
        print("")
        print("  VAMOS ORGANIZAR! Para começarmos, escolha a opção que você deseja.")
        print("--------------------------------------------")
        print("        Para análise de cores, digite 1")
        print("        Para organizações, digite 2 \n")
        print("Digite qualquer outro número para voltar ao menu principal")
        print("--------------------------------------------")
        co = int(input("Insira a sua opção: "))
        if co == 1:
            webbrowser.open('https://color.adobe.com/pt/create/color-wheel/')
            print("--------------------------------------------")
        elif co == 2:
            webbrowser.open('http://marketingparafotografos.com.br/6-dicas-portfolio-fotografia/')
        else:
            print("--------------------------------------------")
    elif opcao == 6:
        print("")
        print("~~~~~~~~ REDES SOCIAIS ~~~~~~~~" .center(130))
        print("")
        print("  Não podemos negar que as redes sociais fazem parte da rotina de muita gente.")
        print("  {}, preparamos um guia para a organização do seu perfil, para isso, escolha uma das redes sociais abaixo.".format(usu))
        print("--------------------------------------------")
        print("        Digite 1, para Twitter")
        print("        Digite 2, para Instagram\n")
        print("Digite qualquer número para voltar ao menu principal.")
        print("")
        soc = int(input("Insira a sua opção: "))
        if soc == 1:
            webbrowser.open('https://i.imgur.com/XyMn7Z8.png')
            print("--------------------------------------------")
        elif soc == 2:
            webbrowser.open('https://i.imgur.com/qUoVJp9.png')
            print("--------------------------------------------")
        else:
            print("--------------------------------------------")
    elif opcao == 7:
        print("")
        print("~~~~~~~~ INSPIRAÇÕES ~~~~~~~~" .center(130))
        webbrowser.open('https://i.imgur.com/olmmxYp.png')
        print("--------------------------------------------")
    elif opcao == 8:
        print("~~~~~~~~GRANDES FOTOGRAFOS~~~~~~~~~".center(130))
        print("------------------------------------")
        print("        Em uma escala de 1 a 10, escolha um número qualquer!")
        print("--------------------------------------------")
        print("Digite qualquer outro número para voltar ao menu principal.")
        print("")
        fot = int(input("Digite o número: "))
        if fot == 1:
            webbrowser.open('http://www.correiobraziliense.com.br/app/noticia/cidades/2015/11/22/interna_cidadesdf,507553/gervasio-baptista-fotojornalista-que-clicou-politicos-misses-e-misse.shtml')
            print("--------------------------------------------")
        elif fot == 2:
            webbrowser.open('http://www.elfikurten.com.br/2015/12/walter-firmo.html')
            print("--------------------------------------------")
        elif fot == 3:
            webbrowser.open('https://en.wikipedia.org/wiki/Helen_Levitt')
            print("--------------------------------------------")
        elif fot == 4:
            webbrowser.open('http://ffw.uol.com.br/noticias/cultura-pop/icones-da-fotografia-german-lorca-e-o-pioneirismo-no-brasil/galeria/2/')
            print("--------------------------------------------")
        elif fot == 5:
            webbrowser.open('https://www.sheilapreebright.com/')
            print("--------------------------------------------")
        elif fot == 6:
            webbrowser.open('http://www.fotografiaprofissional.org/grandes-fotografos-sebastiao-salgado/')
            print("--------------------------------------------")
        elif fot == 7:
            webbrowser.open('http://47canal.us/main.php?1=ma&2=pics')
            print("--------------------------------------------")
        elif fot == 8:
            webbrowser.open('http://www.dianamarkosian.com/opener')
            print("--------------------------------------------")
        elif fot == 9:
            webbrowser.open('http://www.amivitale.com/')
            print("--------------------------------------------")
        elif fot == 10:
            webbrowser.open('http://carriemaeweems.net/')
            print("--------------------------------------------")
        else:
            print("--------------------------------------------")
    else:
        print("")
        print ('Opa, encontramos um testador, parabéns por tentar quebrar nosso programa, estamos gratos por isso!')
        print("Mas esta opção não consta em nosso menu, reveja as opções!")
