import requests
import csv


API_KEY="cdftslaad3idqfmpk0s0cdftslaad3idqfmpk0sg"
API_URL="https://finnhub.io/api/v1"
SYMBOLS = ["AAPL", "AMZN", "NFLX", "META", "GOOGL"]
FIELDS = ["stock_symbol","percentage_change","current_price","last_close_price"]

max_change = (0, "", {})
most_volatile = []

def find_details(symbol):
	r = requests.get(f'{API_URL}/quote?symbol={symbol}&token={API_KEY}')
	if r.status_code == 200:
		res = r.json()
		return res
	return -1

for symbol in SYMBOLS:
	details = find_details(symbol)
	if details != -1:
		if abs(details['dp']) > max_change[0]:
			max_change = (abs(details['dp']), symbol, details)
	else:
		print(f"Error fetching details for {symbol}")
		exit(1)

most_volatile.append([max_change[1], max_change[2]['dp'], max_change[2]['c'], max_change[2]['pc']])

with open("most_volatile.csv", 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(FIELDS)
		csvwriter.writerows(most_volatile)
