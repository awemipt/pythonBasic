# put your python code here


s = input()
digits = [a for a in s if a.isdigit()]
print(*(sorted(set(digits))) if len(digits)> 0 else 'НЕТ')


