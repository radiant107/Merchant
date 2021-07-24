merchant = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入價格： ')
	m =[] # 在大清單裡面設小清單
	m.append(name)
	m.append(price)
	merchant.append(m)
print(merchant)

print(merchant[0][0], merchant[0][1], '元') # 取出大清單的第一個小清單，再取出小清單的第一個和第二個
print(merchant[1][1])


# 簡化小清單寫法
merchant = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入價格： ')
	m =[name, price]
	merchant.append(m)
print(merchant)


# 再更簡化
merchant = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入價格： ')
	merchant.append([name, price])
print(merchant)