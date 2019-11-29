# print('List 1:')
# quan = ['SD','BD','BTL','CG','BD','HBT']
# for i, item in enumerate(quan):
#     print(i+1,'.',quan[i])

# print('List 2:')
# danso = ['SD:150300','BD:247100','BTL:333300','CG:266800','BD:420900','HBT:318000']
# for i, item in enumerate(danso):
#     print(i+1,'.',danso[i])

# ------------------------------------------------------------------

# quan = ['SD:150300','BD:247100','BTL:333300','CG:266800','BD:420900','HBT:318000']
# quan[0] = 150300
# quan[1] = 247100
# quan[2] = 333300
# quan[3] = 266800
# quan[4] = 420900
# quan[5] = 318000
# print(sorted(quan,reverse = True))

# ------------------------------------------------------------------

# quan = ['SD','BD','BTL','CG','BD','HBT']
# danso = [150300, 247100, 333300, 266800, 420900, 318000]
# x = danso[0]
# for i in danso:
#     if x < i:
#         x = i
#     else:
#         pass
# print('Quan co dan so cao nhat:', x)
# y = danso[0]
# for k in danso:
#     if y > k:
#         y = k
#     else:
#         pass
# print('Quan co dan so thap nhat:', y)   

# ------------------------------------------------------------------

# quan = ['SD','BD','BTL','CG','BD','HBT']
# danso = [150300, 247100, 333300, 266800, 420900, 318000]
# x = danso[0]
# for i in danso:
#     if x < i:
#         x = i
#     else:
#         pass
# print('Quan co dan so cao nhat:', quan[danso.index(x)], x)
# y = danso[0]
# for k in danso:
#     if y > k:
#         y = k
#     else:
#         pass
# print('Quan co dan so thap nhat:', quan[danso.index(y)], y)   