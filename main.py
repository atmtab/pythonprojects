access = False
while not access:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == 'Kuma' and password == '12345678':
        print('Access granted')
        access = True
    elif username == 'Kuma':
        print('Access denied, Wrong password')
    else:
        print('Access denied, Wrong username')
print('End of program')