import csv
from statistics import mean

row1 = ['6/20/2019', 'AAPL', 90.91]
row2 = ['6/20/2019', 'MSFT', 41.68]
row3 = ['6/21/2019', 'AAPL', 90.86]
row4 = ['6/20/2019', 'MSFT', 41.51]

result = [row1, row2, row3, row4]

with open('stock_price.csv', mode='w', encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    for row in result:
        writer.writerow(row)

with open('stock_price.csv', mode='r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    df = [line for line in reader]
print(df)

# AAPL 종목의 주식 가격 리스트
apple_prices = [float(item[2]) for item in df if item[1] == 'AAPL']
avg_apple_price = sum(apple_prices) / len(apple_prices)
print(avg_apple_price)

# MSFT 종목의 주식 가격 리스트
msft_prices = [float(item[2]) for item in df if item[1] == 'MSFT']
avg_msft_price = sum(msft_prices) / len(msft_prices)
print(avg_msft_price)

with open('stock_price.csv', mode='r', encoding='UTF-8') as f:
    fieldnames = ['date', 'company', 'price']
    reader = csv.DictReader(f, fieldnames=fieldnames)
    df = [line for line in reader]
print(df)

# aapl 평균
aapl_price = [float(item['price']) for item in df if item['company'] == 'AAPL']
avg_aapl_price = sum(apple_prices) / len(apple_prices)
print(avg_aapl_price)

# msft 평균
msft_price = [float(item['price']) for item in df if item['company'] == 'MSFT']
avg_msft_price = sum(msft_prices) / len(msft_prices)
print(avg_msft_price)



