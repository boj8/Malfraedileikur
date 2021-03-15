#Til þess að nota forritið þarf að keyra þessa skrá
import csv
from menu import menu

print('Velkomin/n í málkennslu!')
print('Augnablik...', end='\r')

#Beygingarmyndir lesnar inn
with open('SHsnid.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=';')
    bmyndir = list(reader)

#Lýsing á tögum lesin inn
with open('tags.csv', 'r', encoding='utf8') as f:
    reader = csv.reader(f, delimiter=';')
    tags = list(reader)

#Geymir nöfn orðflokka
ordflokkar = {
    'ao': 'atviksorð',
    'fn': 'fornafn',
    'hk': 'hvorugkynsnafnorð',
    'kk': 'karlkynsnafnorð',
    'kvk': 'kvenkynsnafnorð',
    'lo': 'lýsingarorð',
    'so': 'sagnorð'
}

#Biður notanda að velja leik og kallar á valmynd fyrir valinn leik
def velja():
    print('Sláðu inn beygja til að æfa þig í beygingu.')
    print('Sláðu inn flokkar til að æfa þig í orðflokkum.')
    val = input()
    if(val == 'beygja'):
        print('\n')
        menu(bmyndir, ordflokkar, tags, True)
    elif(val == 'flokkar'):
        print('\n')
        menu(bmyndir, ordflokkar, tags, False)
    else:
        velja()

velja()