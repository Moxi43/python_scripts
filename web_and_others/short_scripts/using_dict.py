ab = { 'Swaroop' : 'swaroop@swaroopch.com',
       'Larry'   : 'lary@wall.org',
       'Matsumoto' : 'matz@ruby-lang.org',
       'Spammer' : 'spammer@hotmail.com'
      }
print("Адрес Swaroop'a:",ab['Swaroop'])
del ab['Spammer']
print('\nВ адресной книге {0} контактов\n'.format(len(a,b)))
for name, adress in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, adress))
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nАдресс Guido:", ab['Guido'])
