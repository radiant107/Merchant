merchant = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入價格： ')
	price = int(price)
	merchant.append([name, price])
print(merchant)

print(merchant[0][0], '的價格是', merchant[0][1], '元') 

with open('merchant.csv', 'w', encoding = 'utf-8') as f: # 寫入
	f.write('商品,價格\n')
	for m in merchant:
		f.write(m[0] + ',' + str(m[1]) + '\n') # CSV檔在excel中用逗點做區隔，電腦才看得懂會自動分格
		                                              # 字串跟字串合併中間用+號

