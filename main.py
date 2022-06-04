print('''Numeral System Counters, by asiancart''')

while True:
    response = input('Enter the starting number > ')
    if response == '':
        response = 0
        break
    if response.isdecimal():
        break
    print('Please enter a number greater than or equal to 0.')
start= int(response)

while True:
    response = input('Enter how many numbers to display > ')
    if response == '':
        response = 1000
        break
    if response.isdecimal():
        break
    print('please enter a number.')
amount=int(response)

for number in range(start,start+amount):
    hexNumber= hex(number)[2:].upper()
    binNumber = bin(number)[2:]

    print('DEC:',number, '   HEX:', hexNumber, '   BIN:', binNumber)