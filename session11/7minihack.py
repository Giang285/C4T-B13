character = {
    'Name:': 'Light',
    'Age:': 17,
    'Strength:': 8,
    'Defense:': 10,
    'HP:': 100,
    'Backpack:': ['Shield', 'Bread Loaf'],
    'Gold:': 100,
    'Level:': 2
}
character['Gold:'] + 50
character['Backpack:'].append('Flintstone')
character['Pocket:'] = ['MonsterDex','Flashlight']
for i,a in enumerate(character):
    print(i+1,a,character[a],)