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

loaimay = input('loai may ban muon mua la:')
number = input('So luong ma ban muon mua la:')
if loaimay in price and number.isalpha:
    print('Voi loai may la: ',loaimay,'co so luong la: ',computer[loaimay], 'tong so tien la: ',price[loaimay]*int(number))
    computer[loaimay] =  computer[loaimay] - int(number) 
    print('So luong may con lai la:',computer)
else:
    print('So luong hoac loai may ko hop le!')   