price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJITSU' : 900,
    'ALIENWARE' : 1000    
}
computer = {
    'HP' : 20,
    'DELL' : 60,
    'MACBOOK' : 10,
    'ASUS' : 30,
    'TOSHIBA' : 10,
    'FUJITSU' : 15,
    'ALIENWARE' : 5
}

print('bang gia cua ASUS la: ',price['ASUS'])

#----------------------------------------------------------------------------
price = {
    'HP' : 600,
    'DELL' : 650,
    'MACBOOK' : 12000,
    'ASUS' : 400,
    'ACER' : 350,
    'TOSHIBA' : 600,
    'FUJITSU' : 900,
    'ALIENWARE' : 1000    
}
computer = {
    'HP' : 20,
    'DELL' : 60,
    'MACBOOK' : 10,
    'ASUS' : 30,
    'TOSHIBA' : 10,
    'FUJITSU' : 15,
    'ALIENWARE' : 5
}

a = input('ban muon xem loai may gi: ')
if a in price:
    print('bang gia cua may ban chon la: ',price[a])
else:
    print('ko co thong tin')    
