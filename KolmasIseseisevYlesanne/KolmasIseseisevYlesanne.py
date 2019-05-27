from datetime import datetime
# repush

def add_data_user():
    new_data = ['', '']
    while len(new_data) != 2 or not new_data[0].isalpha() or not new_data[1].isnumeric():
        new_data = input('\tFikseerige sade kujul [Identifikaator][20](C): ')
        if new_data == 'C':
            break
        new_data = new_data.split(']')
        if len(new_data) == 3 and new_data[-1] == '' and new_data[0][0] == '[' and new_data[1][0] == '[':
            del new_data[-1]
            new_data[0] = new_data[0][1:]
            new_data[1] = new_data[1][1:]
    if new_data == 'C':
        print()
        return
    time = str(datetime.now().time())
    time = time[:8]
    date = str(datetime.now().date())
    date = date.replace('-', '.')
    date = date[8:10] + date[4:8] + date[:4]
    entry = date + ' ' + time + '-[' + new_data[0] + '][' + new_data[1] + ']'
    return entry

def add_data():
    entry = add_data_user()
    with open('andmebaas.txt', 'a', encoding='utf-8') as file:
        file.write(entry + '\n')
    print('\tSade fikseeritud!')
    print()

def change_data():
    content = ''
    dates = []
    with open('andmebaas.txt', 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            dates.append(line[:20])
            content += '\t\t' + str(i + 1) + '.' + line[20:]
    print('\tAndmebaasis olevad andmed:')
    print(content)
    if len(content) > 0:
        content = content.split('\n')
        del content[-1]
    change = 0
    while 0 >= int(change) or int(change) > len(content):
        change = input('\tSisestage sademe indeks, mida soovite muuta (C): ')
        if change == 'C':
            break
        if not change.isnumeric():
            change = 0
            continue
        if 0 >= int(change) or int(change) > len(content):
            print('\t\tSisestatud sademe indeksit ei eksisteeri andmebaasis!')
    if change == 'C':
        return
    entry = add_data_user()
    content[int(change) - 1] = entry
    with open('andmebaas.txt', 'w', encoding='utf-8') as file:
        for i, line in enumerate(content):
            if i != int(change) - 1:
                file.write(dates[i] + line[4:] + '\n')
            else:
                file.write(line + '\n')
    print('\tSeadme kirje on uuendatud!')
    print()

def database_content():
    content = []
    with open('andmebaas.txt', 'r', encoding='utf-8') as file:
        for line in file:
            content.append(line[:-1])
    print('\tAndmebaasi sisu:')
    for line in content:
        print('\t\t' + line)
    print()

def user_input(commands):
    while True:
        user = ''
        while user not in commands:
            user = input('Sisestage soovitud valik ({0}, {1}, {2}, {3}): '.format(commands[0], commands[1], commands[2], commands[3]))
        print()
        if user == commands[0]:
            add_data()
        elif user == commands[1]:
            change_data()
        elif user == commands[2]:
            database_content()
        elif user == commands[3]:
            close = input('\tKas olete kindel, et soovite programmi sulgeda (\'jah\')? ')
            if close.lower() == 'jah':
                print('\tProgramm läks kinni!')
                break
            print()

def start():
    try:
        with open('andmebaas.txt', 'r', encoding='utf-8') as file: pass
    except OSError:
        with open('andmebaas.txt', 'w', encoding='utf-8') as file: pass
    commands = ['L', 'M', 'P', 'E']
    print('{0} - Sademete lisamine andmebaasi.'.format(commands[0]))
    print('{0} - Andmebaasis oleva sademe muutmine.'.format(commands[1]))
    print('{0} - Andmebaasis asuvate sademete kuvamine.'.format(commands[2]))
    print('{0} - Programmi sulgemine.'.format(commands[3]))
    print()
    user_input(commands)

start()
