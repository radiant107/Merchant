merchant = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入價格： ')
	merchant.append([name, price])
print(merchant)

print(merchant[0][0], '的價格是', merchant[0][1], '元') 

with open('merchant.csv', 'w') as f: # 寫入
	for m in merchant:
		f.write(m[0] + ',' + m[1] + '元' + '\n') # CSV檔在excel中用逗點做區隔，電腦才看得懂會自動分格

