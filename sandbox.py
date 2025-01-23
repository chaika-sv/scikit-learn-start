vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхцчшщъь'
s = ''
a = input('Введите пароль:')
for c in a:
    if c in vowels:
        s = s + '0'
    elif c in consonants:
        s = s + '1'

print(s)
