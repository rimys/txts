line = ''
with open('guest.txt', 'a') as guests:
    while line != 'exit':
        line = input('Введите своё имя: ')
        #line += '\n'
        guests.write(line)
        guests.write('\n')