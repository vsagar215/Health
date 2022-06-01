from datetime import datetime
import json

now = datetime.now()
date = now.strftime('%m') + '/' + now.strftime('%d')
daily = int(input('Enter calorie total: '))

with open("calorie_log.json", "r+") as f:
	data = json.load(f)
	data[date] = daily
	f.seek(0)
	json.dump(data, f)