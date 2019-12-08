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

skill = {
    'Skill 1:' : {
        'Name' : 'Tackle',        
        'Minimum level' : 1,
        'Damage' : 5,
        'Hit rate' : 0.3        
    },
    'Skill 2:' : {
        'Name' : 'Quick attack',        
        'Minimum level' : 2,
        'Damage' : 3,
        'Hit rate' : 0.5        
    },
    'Skill 3:' : {
        'Name' : 'Strong kick',        
        'Minimum level' : 4,
        'Damage' : 9,
        'Hit rate' : 0.2        
    }
}
import random
c = random.randint(0,1)    
b = input('Skill ban muon dung: ')
if b == 1  and character['Level:'] >= skill['Skill 1:']['Minimum level']:
    if c > skill['Skill 1:']['Hit rate']:
        print('HIT!!','sat thuong ban gay ra la:',skill['Skill 1:']['damage']) 
    else:
        print('Skill cua ban da truot')     
elif b == 2  and character['Level:'] >= skill['Skill 2:']['Minimum level']:
    if c > skill['Skill 2:']['Hit rate']:
        print('HIT!!','sat thuong ban gay ra la:',skill['Skill 2:']['damage']) 
    else:
        print('Skill cua ban da truot')
elif b == 3 and character['Level:'] >= skill['Skill 3:']['Minimum level']:
    if c > skill['Skill 3:']['Hit rate']:
        print('HIT!!','sat thuong ban gay ra la:',skill['Skill 3:']['damage']) 
    else:
        print('Skill cua ban da truot')
else:
    print('Skill chua xac dinh!')

