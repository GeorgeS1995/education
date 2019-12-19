ab = {'swaroop' : 'swaroop@swaroop.com',
      'larry' : 'larry@larry.org',
      'matilda' : 'matilda',
      'spammer' : 'spammer'}

print("swaroop's addresse is {}".format(ab['swaroop']))

del ab['spammer']

print('\n There is a {} contacts in a book'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} have address {1}'.format(name, address))

ab ['Pedro'] = 'Pedro@pedro.com'

for name, address in ab.items():
    if name == 'Pedro':
        name = 'Pedro'
        print('{0} address is {1}'.format(name, ab[name]))
