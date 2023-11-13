import csv
# It contains the Data for analytics
stock_csv=r'/Users/abhishekjhawar/Desktop/Project/DashBoard/stock1.csv'

with open(stock_csv,encoding="utf-8") as csvfile:
   reader=csv.DictReader(csvfile)
   Date={'Date':[]}
   Open={'Open':[]}
   High={'High':[]}
   Low={'Low':[]}
   Close={'Close':[]}
   Adj_Close={'Adj_Close':[]}
   Volume={'Volume':[]}
   for r in reader:
      Date['Date'].append(r['Date'])
      Open['Open'].append(format(eval(r['Open']),'.2f'))
      High['High'].append(format(eval(r['High']),'.2f'))
      Low['Low'].append(format(eval(r['Low']),".2f"))
      Close['Close'].append(format(eval(r['Close']),'.2f'))
      Adj_Close['Adj_Close'].append(format(eval(r['Adj_Close']),".2f"))
      Volume['Volume'].append(format(eval(r['Volume']),".2f"))
