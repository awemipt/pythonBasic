from string import ascii_lowercase

def isValidEmail(s: str):
    s = s.lower()
    chars = ascii_lowercase + '_@.1234567890'
    if set(s) - set(chars):
        return False
    if s.count('@') > 1 or s.count('.') > 1:
        return False
    if '.' not in s.split('@')[1]:
        return False
    return True


emails = input().split()
print(*filter(isValidEmail, emails))