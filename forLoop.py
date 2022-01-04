'''
for AnyLetter in 'StenTechy':
    print(AnyLetter)'''

myList = ['Tems','Shakira','Eilish','Tiwa']
my_dict = {
    'name': 'Sten',
    'age': 20,
    'nationality': 'Mars',
    'Hobby': 'Tinkering',
    'friends': ['Sten', 'Stephen', 'StenTechy', 'Situben']
}

for artist in myList:
    if artist == 'Eilish':
        break
    print(artist)
    
print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

for infos in my_dict:
    if infos == 'nationality':
        break
    print(infos)
