from datetime import datetime

#Fall sem skráir árangur notanda í textaskrá, tekur inn árangur og valinn leik
def writescore(score, leikur):
    if(leikur):#Velur rétta textaskrá    
        scores = open('bscore.txt','a', encoding='utf8')
    else:
        scores = open('fscore.txt','a', encoding='utf8')
    #Skráir árangur og tíma í textaskrá
    scores.write(str(score) + ';')
    date = datetime.now()
    scores.write(str(date.day) + '. ' + str(date.month) + '. ' + str(date.year) + ' ' + str(date.hour) + ':' + str(date.minute) + '\n')

#Fall sem birtir besta árangur notanda, tekur inn valinn leik
def viewscore(leikur):
    if(leikur):#Velur rétta textaskrá    
        text = open('bscore.txt', 'r', encoding='utf8')
    else:    
        text = open('fscore.txt', 'r', encoding='utf8')
    #Les textaskrá og setur innihaldið í lista
    scores = text.read()
    scores = scores.split('\n')
    del scores[-1]
    for i in range(len(scores)):
        scores[i] = scores[i].split(';')
    
    scores.sort(reverse=True)#Árangri raðað í lækkandi röð
    if(len(scores) == 0):
        print('Enginn árangur skráður')
    else:#Birtir allt að 10 bestu árangra notanda
        magn = min(len(scores), 10)
        print('Þinn besti árangur:')
        for i in range(magn):
            print(str(i + 1) + '. ' + scores[i][0] + ' rétt, ' + scores[i][1])

    input('Ýttu á enter til að fara til baka\n')