import matplotlib.pyplot as plt
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

data = json.load(open("calorie_log.json", "r"))
f, ax = plt.subplots(figsize=(15,9))
ax.set_xlabel('Date')
ax.set_ylabel('Calories consumed')

plt.plot(data.keys(), data.values(), color='#2B709F', marker="o")
plt.axhline(y=2000, color="#C23737", ls="--")
plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.savefig("calorie_plot.png")
plt.show()
