computer = {
    'HP' : 20,
    'DELL' : 50,
    'MACBOOK' : 12,
    'ASUS' : 30
}

a = input('Hang may tinh ma ban muon kiem tra: ')

if a == 'HP' or a == 'hp':
    print('So luong co trong kho la ', computer['HP'])
elif a == 'DELL' or a== 'dell':
    print('So luong co trong kho la ', computer['DELL'])
elif a == 'MACBOOK' or a == 'macbook':
    print('So luong co trong kho la ', computer['MACBOOK'])
elif a == 'ASUS' or a == 'asus':
    print('So luong co trong kho la ', computer['ASUS'])
else:
    print('May khong co trong kho!')


