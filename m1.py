# 讀取檔案
merchant = []
with open('merchant.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue            # 跳過這回不要 
		name, price = line.strip().split(',') # 先去除分行符號再針對逗號做切割，切割完後會自動變成清單
		merchant.append([name, price])

print(merchant[0][0], '價格是', merchant[0][1])
for m in merchant:
	print(m[0], '的價格是', m[1], '元') 

# 讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入價格： ')
	price = int(price)
	merchant.append([name, price])

# 寫入檔案
with open('merchant.csv', 'w', encoding = 'utf-8') as f: # 寫入
	f.write('商品,價格\n')
	for m in merchant:
		f.write(m[0] + ',' + str(m[1]) + '\n') # CSV檔在excel中用逗點做區隔，電腦才看得懂會自動分格
		                                              # 字串跟字串合併中間用+號

