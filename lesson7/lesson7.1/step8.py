def verifyEmail(email):
    email = email.lower
    st = set('abcdefghijklmnopqrstuvwxyz123456789_@.')
    if '@' not in email or '.' not in email:
        print('НЕТ')
    else:
        for letter in email:
            if letter not in st:
                print('НЕТ')
                break
        else:
            print("ДА")


email = input()
verifyEmail(email)
