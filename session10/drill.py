#drill 1

# worterbuch = {
#     'Hund' : 'Dog',
#     'Auto' : 'Car',
#     'Jahr' : 'Year',
#     'Achtung' : 'Attention'
# }
# while True:
#     a = input('Ban muon tra phan gi?')
#     if a in worterbuch:
#         print(a, 'co nghia la:', worterbuch[a])
#     else:
#         print('Khong co trong tu dien!')
# break

#-----------------------------------------------------------
#drill 2

# worterbuch = {
#     'Hund' : 'Dog',
#     'Auto' : 'Car',
#     'Jahr' : 'Year',
#     'Achtung' : 'Attention'
# }

#----------------------------------------------------------
#drill 5

# a = {'name' : 'HUY',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.8
# }                        
# b = {'name' : 'TUNG',
#     'Role' : 'Cook',
#     'Hours' : 24,
#     'salary per hours($)' : 1.5
# }                                        
# c = {'name' : 'M.DUC',
#     'Role' : 'Manager',
#     'Hours' : 20,
#     'salary per hours($)' : 2
# }
# nhanvien = [a,b,c]
# print(nhanvien) 

#----------------------------------------------------------
#Drill 5

# a = {'name' : 'HUY',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.8
# }                        
# b = {'name' : 'TUNG',
#     'Role' : 'Cook',
#     'Hours' : 24,
#     'salary per hours($)' : 1.5
# }                                        
# c = {'name' : 'M.DUC',
#     'Role' : 'Manager',
#     'Hours' : 20,
#     'salary per hours($)' : 2
# }
# d = {'name' : 'DON',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.9
# }                        
# e = {'name' : 'H.DUC',
#     'Role' : 'Waiter',
#     'Hours' : 14,
#     'salary per hours($)' : 0.7
# }                                     
# nhanvien = [a,b,c,d,e]
# print(nhanvien) 

#------------------------------------------------------------

# a = {'name' : 'HUY',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.8
# }                        
# b = {'name' : 'TUNG',
#     'Role' : 'Cook',
#     'Hours' : 24,
#     'salary per hours($)' : 1.5
# }                                        
# c = {'name' : 'M.DUC',
#     'Role' : 'Manager',
#     'Hours' : 20,
#     'salary per hours($)' : 2
# }
# d = {'name' : 'DON',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.9
# }                        
# e = {'name' : 'H.DUC',
#     'Role' : 'Waiter',
#     'Hours' : 14,
#     'salary per hours($)' : 0.7
# }                                     
# nhanvien = [a,b,c,d,e]
# nhanvien.pop(2)
# print(nhanvien) 

#------------------------------------------------------------

# a = {'name' : 'HUY',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.8
# }                        
# b = {'name' : 'TUNG',
#     'Role' : 'Cook',
#     'Hours' : 24,
#     'salary per hours($)' : 1.5
# }                                        
# c = {'name' : 'M.DUC',
#     'Role' : 'Manager',
#     'Hours' : 20,
#     'salary per hours($)' : 2
# }
# d = {'name' : 'DON',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.9
# }                        
# e = {'name' : 'H.DUC',
#     'Role' : 'Waiter',
#     'Hours' : 14,
#     'salary per hours($)' : 0.7
# }                                     
# nhanvien = [a,b,c,d,e]
# for i in enumerate(nhanvien):
#     print(i) 

#------------------------------------------------------------

# a = {'name' : 'HUY',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.8
# }                        
# b = {'name' : 'TUNG',
#     'Role' : 'Cook',
#     'Hours' : 24,
#     'salary per hours($)' : 1.5
# }                                        
# c = {'name' : 'M.DUC',
#     'Role' : 'Manager',
#     'Hours' : 20,
#     'salary per hours($)' : 2
# }
# luongthang = {
#     'luong thang HUY' : 0.8*12*4,
#     'luong thang TUNG' : 1.5*24*4,
#     'luong thang M.DUC' : 2*20*4
# }
# print(luongthang)

#------------------------------------------------------------

# a = {'name' : 'HUY',
#     'Role' : 'Waiter',
#     'Hours' : 12,
#     'salary per hours($)' : 0.8
# }                        
# b = {'name' : 'TUNG',
#     'Role' : 'Cook',
#     'Hours' : 24,
#     'salary per hours($)' : 1.5
# }                                        
# c = {'name' : 'M.DUC',
#     'Role' : 'Manager',
#     'Hours' : 20,
#     'salary per hours($)' : 2
# }
# luongthang = {
#     'luong thang HUY' : 0.8*12*4,
#     'luong thang TUNG' : 1.5*24*4,
#     'luong thang M.DUC' : 2*20*4
# }
# tongluongthang = {
#     luongthang['luong thang HUY'] + luongthang['luong thang TUNG'] + luongthang['luong thang M.DUC']
# }
# print('Tong luong ma 1 thang nguoi ta tra cho cac nhan vien la : ',tongluongthang)

#------------------------------------------------------------
#drill 8

# a = {
#     'A Game of Thrones' : 'phat hanh 1996', 
#     'nhan vat' : 'Ned Stark, Jon Snow, Arya Stark, Daenerys Targaryen,... '
# }
# b = { 
#     'Dredd' : 'phat hanh 2012', 
#     'dien vien tham gia : Karl Urban, Lena Headey, Olivia Thirlby'
# }    
# a['Quoc gia'] = 'Hoa Ki'
# b['hang san suat'] = 'DNA Film'
# c = [a,b]
# print(c) 

#------------------------------------------------------------
# GoT = {
#     'Ten' : 'A Game of Thrones',
#     'Nam xuat ban' : '1996',
#     'nhan vat' : ['Ned Stark', 'Jon Snow', 'Arya Stark', 'Daenerys Targaryen']
# }
# for i,a in enumerate(GoT):
#     print(i+1,a,GoT[a],sep = '-')

#------------------------------------------------------------

# GoT = {
#     'Ten' : 'A Game of Thrones',
#     'Nam xuat ban' : '1996',
#     'nhan vat' : ['Ned Stark', 'Jon Snow', 'Arya Stark', 'Daenerys Targaryen']
# }
# x = input('Nhan vat moi: ')
# GoT['nhan vat'].append(x)
# print(GoT['nhan vat'][1])

#------------------------------------------------------------

# GoT = {
#     'Ten' : 'A Game of Thrones',
#     'Nam xuat ban' : '1996',
#     'nhan vat' : ['Ned Stark', 'Jon Snow', 'Arya Stark', 'Daenerys Targaryen']
# }
# for b,c in enumerate(GoT['nhan vat']):
#     print(b+1,c)

#------------------------------------------------------------

# GoT = {
#     'Ten' : 'A Game of Thrones',
#     'Nam xuat ban' : '1996',
#     'nhan vat' : ['Ned Stark', 'Jon Snow', 'Arya Stark', 'Daenerys Targaryen']
# }
# for b,c in enumerate(GoT):
#     print(b+1,c,GoT[c])

#------------------------------------------------------------
