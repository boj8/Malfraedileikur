import random

#Fall sem býr til spurningar, tekur inn lista af beygingarmyndum, nöfn orðflokka, lýsingar á tögum og hvaða leik er verið að spila
def spurning(bmyndir, ordflokkar, tags, leikur):
    ord = bmyndir[random.randrange(len(bmyndir))]#Beygingarmynd valin af handahófi úr beygingarmyndalista
    lysing = "" #Geymir lýsingu beygingarmyndar
    uppflord = ord[0]#Geymir uppflettiorð valinnar beygingarmyndar
    ordfl = ord[2]#Geymir orðflokk valinnar beygingarmyndar
    bmynd = ord[4]#Geymir valda beygingarmynd
    tag = ord[5]#Geymir tag valinnar beygingarmyndar
    
    if(leikur):#Býr til spurningu um beygingu
        for i in tags:#Finnur lýsingu beygingarmyndarinnar
            if(ordfl == i[0] and tag == i[1]):
                lysing = i[2]
                break
        
        svar = input('Skrifaðu ' + ordflokkar[ordfl] + 'ið ' + uppflord + ' í ' + lysing + '.\n')#Tekur við svari frá notanda
        if(svar == 'h'):#Skipunin h er notuð til að hætta
            print('\n')
            return 2
        elif(svar == bmynd):
            print("Rétt svar\n")
            return 1
        else:
            print('Rangt svar, rétt svar er ' + bmynd + '\n')
            return 0
    
    else:#Býr til orðflokkaspurningu
        svar = input('Hvaða orðflokki tilheyrir orðið ' + uppflord + '?\n')
        if(svar == 'h'):#Skipunin h er notuð til að hætta
            print('\n')
            return 2
        elif(svar == ordfl or svar == ordflokkar[ordfl]):
            print("Rétt svar\n")
            return 1
        else:
            print('Rangt svar, rétt svar er ' + ordfl + ', ' + ordflokkar[ordfl] + '\n')
            return 0