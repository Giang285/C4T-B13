items = ['40k', 'wargame', 'GoT', 'Joker']

while True:
    luachon = input('Ban muon lam gi?')
    if luachon == 'c':
        x = input('Ban muon them phan tu nao?')
        items.append(x)
        print(items)
    if luachon == 'r':
        if items == 0:
            print('Khong co phan tu nao')
        for item in enumerate(items):
            print(*item) 
    if luachon == 'u':
        a = len(items)
        b = int(input('ban muon nang cap phan tu thu may?'))
        if b < a :
            items[b] = input('ban muon thay doi la gi?')
            print(items)
        elif b > a:
            print('phan tu thay doi ko phu hop') 
    if luachon == 'd':
        c = int(input('ban muon xoa phan tu thu may?'))
        d = len(items)
        if c < d:
            items.pop(c)
            print(items)
        elif c > d:
            print('phan tu muon xoa ko phu hop')
    else:
        print('ban phai chon dung yeu cau')        
