import os

# 讀取檔案
def read_file(filename):
	merchant = []
	with open(filename, 'r', encoding='utf-8') as list0:	
		for line in list0:
			if '商品,價格' in line:
				continue            
			name, price = line.strip().split(',') 
			merchant.append([name, price])
	return merchant
	
# 列印檔案
def print_file(merchant):
	print('現在的清單如下：')
	for m in merchant:
		print(m[0], '的價格是', m[1], '元')
	
# 讓使用者輸入
def input_file(merchant):
	while True:
		name = input('請輸入商品名稱： ')
		if name == 'q':
			break
		price = input('請輸入價格： ')
		price = int(price)
		merchant.append([name, price])
	return merchant

# 寫入檔案
def write_file(filename, merchant):# 寫入檔案
	with open(filename, 'w', encoding = 'utf-8') as list1:
		list1.write('商品,價格\n')
		for m in merchant:
			list1.write(m[0] + ',' + str(m[1]) + '\n') 

def main():	
	filename = 'merchant.csv'
	merchant = []
	if os.path.isfile(filename):   # 檢查相對路徑有沒有檔案
		print('很好，找到檔案，讀取中...')
		merchant = read_file(filename)
		print_file(merchant)
	else:
		print('找不到檔案...，請重新開始輸入')
	merchant = input_file(merchant)
	write_file(filename, merchant)


main()