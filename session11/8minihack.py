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
for i,a in enumerate(skill):
    print(i+1,a,skill[a])