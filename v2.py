def encode_text(text):
    returnvar = str()
    for a in text[::-1]:
        returnvar = returnvar + chr((ord(a) + 1) * 2)
    else:
        return returnvar


def decode_text(text):
    returnvar = str()
    for a in text[::-1]:
        returnvar = returnvar + chr(int(ord(a) / 2) - 1)
    else:
        return returnvar


print('Welcome to Bsides vault. In here we store flags for challanges\nThe current amount of flags in database is: 1')
username = input('Enter username: ')
password = input('Enter password: ')
if password == "a" and username == 'admin':
    print('\nWelcome admin,')
    flag = 'BSP{' + decode_text('bæâæhlæhîhæ') + '}'
    msg = f"\n+-------------------------------+\n| Length: 1                     |\n|                               |\n| Bsides Vault: {flag}|\n|                               |\n+-------------------------------+\n    "
    print(msg)
else:
    if username == 'admin':
        print('\nWrong password!')
    else:
        print('\nWrong username or password!')
