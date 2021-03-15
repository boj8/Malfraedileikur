from spurning import spurning
import time
import highscore

#Fall sem birtir valmynd fyrir valinn leik og spyr spurninga
def menu(bmyndir, ordflokkar, tags, leikur):
    if(leikur):#Beygingaleikur
        print('Þú átt að beygja eins mörg orð í uppgefnu falli, kyni, tölu o.s.frv. og þú getur á 60 sekúndum.')
    else:#Orðflokkaleikur
        print('Þú átt að giska á réttan orðflokk(og kyn) eins margra orða og þú getur á 60 sekúndum.')
        print('Orðflokkarnir eru:')
        for i, j in ordflokkar.items():
            print(i + ': ' + j, end=', ')
        print('\b\b.')
    print('Sláðu inn spila til að spila.')
    print('Sláðu inn æfa til að æfa þig.')
    print('Sláðu inn árangur til að skoða þinn besta árangur.')
    print('Sláðu inn skipta til að skipta um leik.')
    print('Sláðu inn h til að hætta.')
    
    skipun = input()#Tekur við skipun frá notanda
    
    if(skipun == 'h'):
        exit()
    elif(skipun == 'æfa'):#Birtir spurningar þangað til notandi velur að hætta
        print('\n')
        print('Þú getur æft þig eins lengi og þú vilt, sláðu inn h þegar þú vilt hætta.')
        while(True):
            if(spurning(bmyndir, ordflokkar, tags, leikur) == 2):#Spurning skilar 2 þegar notandi vill hætta
                break
    elif(skipun == 'spila'):#Birtir spurningar þangað til 60 sekúndur eru liðnar eða notandi velur að hætta
        print('\n')
        rett = 0#Geymir fjölda réttra svara
        svar = 0#Geymir svar notanda
        timi = time.time()#Tími þegar leikur hefst
        endir = timi + 60#Tími þegar leikur endar
        while(time.time() < endir):#Lykkja sem endar þegar tíminn er liðinn
            svar = spurning(bmyndir, ordflokkar, tags, leikur)
            if(svar == 2):
                break
            rett += svar
        print('Tíminn er búinn, þú svaraðir ' + str(rett) + ' rétt.\n')#Fjöldi réttra svara birtur
        highscore.writescore(rett, leikur)#Árangur skráður
    elif(skipun == 'árangur'):#Birtir besta árangur notandans
        print('\n')
        highscore.viewscore(leikur)
    elif(skipun == 'skipta'):#Skiptir um leik
        print('\n')
        menu(bmyndir, ordflokkar, tags, not leikur)
    
    menu(bmyndir, ordflokkar, tags, leikur)