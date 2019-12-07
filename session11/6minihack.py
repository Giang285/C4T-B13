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

a = 0
for i in computer:
    a += computer[i]*price[i]
print('tong tai san cua cua hang la',a)