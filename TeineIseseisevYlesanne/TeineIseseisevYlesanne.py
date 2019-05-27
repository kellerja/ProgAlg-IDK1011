def järved(parv, järveNimi, hanedeArv):
    jätka = True
    järv = ''
    while not järv.isnumeric() or jätka:
        järv = input('Mitu hane maandub \'{0}\' parvest {1}ele? '.format(parveNimed[parv], järveNimi))
        if järv.isnumeric() and int(järv) > hanedeArv:
            jätka = True
            print('\tParves \'{0}\' ei ole nii palju hanesid!'.format(parveNimed[parv]))
            print('\tParves \'{0}\' on {1} hane!'.format(parveNimed[parv], hanedeArv))
            print('\tSisestage väiksem väärtus!')
        else:
            jätka = False
    hanedeArv -= int(järv)
    print('\t{0}ele maandus {1} hane ja {2} hane lendab edasi!'.format(järveNimi, järv, hanedeArv))
    parveLiikumine[parv].append(järv)
    return hanedeArv

def parveNimiJaHulk(index):
    punctuation = ['£', 'ˇ', '§', '~', '¤', '`', '´', '\n', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    nimi = '0'
    jätka = True
    print('\tSisestage {0}. haneparve ...'.format(index + 1))
    while nimi.isnumeric() or jätka:
        nimi = input('\t\t... nimi: ')
        for täht in nimi:
            if täht in punctuation:
                jätka = True
                break
            jätka = False
    parveNimed.append(nimi)
    arv = ''
    while not arv.isnumeric():
        arv = input('\t\t... liikmete arv: ')
    parveLiikmed.append(arv)
    parveLiikumine.append([])

def lõpetamine():
    lõpetamine = input('Kas soovite jätkata (jah/ei)? ')
    if lõpetamine.lower() == 'jah':
        print()
        hanedeJälgimine()
    else:
        print("Programm läks kinni!")
        return 1

def hanedeJälgimine():
    järvedeNimed = ['Endla järv', 'Saadjärv', 'Ratva järv']
    järvedelHaned = []
    hanedeKoguArv = 0
    lõpeta = 0
    global haneparved
    haneparved = ''
    global parveNimed
    parveNimed = []
    global parveLiikmed
    parveLiikmed = []
    global parveLiikumine
    parveLiikumine = []
    while not haneparved.isnumeric():
        haneparved = input('Mitu haneparve on nähtud? ')
    for i in range(int(haneparved)):
        parveNimiJaHulk(i)
    #print()
    print('Lõunasse lähevad järgmised haneparved:')
    for parv in range(int(haneparved)):
        print('\t\'{0}\' ({1} hane)'.format(parveNimed[parv], parveLiikmed[parv]))
    for i in range(len(järvedeNimed)):
        järvedelHaned.append(0)
    for parv in range(int(haneparved)):
        hanedeArv = int(parveLiikmed[parv])
        for i in range(len(järvedeNimed)):
            hanedeArv = järved(parv, järvedeNimed[i], hanedeArv)
            järvedelHaned[i] += int(parveLiikumine[parv][i])
        hanedeKoguArv += int(parveLiikmed[parv])
    print()
    for i in range(len(järvedeNimed)):
        print('{0}ele on maandunud kokku {1} hane!'.format(järvedeNimed[i], järvedelHaned[i]))
    print('Eesti järvedel ei peatunud {0} hane!'.format(hanedeKoguArv - sum(järvedelHaned)))
    print()
    lõpeta = lõpetamine()
    if lõpeta == 1 or lõpeta is None:
        return

hanedeJälgimine()
