morze = {'А': ".-",
         'М': '--',
         'Ш': '----',
         'Б': '-...',
         'Н': '-.',
         'Щ': '--.-',
         'В': '.--',
         'О': '---',
         'Ъ': '--.--',
         'Г': '--.', 'П': '.--.', 'Ы': '-.--',
         'Д': '-..', 'Р': '.-.', 'Ь': '-..-',
         'Е': '.', 'Ё': '.', 'С': '...', 'Э': '..-..',
         'Ж': '...-', 'Т': '-', 'Ю': '..--',
         'З': '--..', 'У': '..-', 'Я': '.-.-',
         'И': '..', 'Ф': '..-.', ' ': '-...-',
         'Й': '.---', 'Х': '....',
         'К': '-.-', 'Ц': '-.-.',
         'Л': '.-..', 'Ч': '---.'}
s = list(input().upper())
d =[]
for sim in s:
    d.append(morze[sim])
print(" ".join(d))
