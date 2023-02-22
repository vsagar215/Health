## NEEDS: NEW PATCH -- CUMULATIVE WEEKS TOTAL

import matplotlib.pyplot as plt
from datetime import datetime
import json

from sympy import rotations

now = datetime.now()
date = now.strftime('%m') + '/' + now.strftime('%d')
daily = int(input('Enter calorie total: '))

with open("calorie_log.json", "r+") as f:
	data = json.load(f)
	data[date] = daily
	f.seek(0)
	json.dump(data, f)

data = json.load(open("calorie_log.json", "r"))
####
# f, ax = plt.subplots(figsize=(15,9))
# ax.set_xlabel('Date')
# ax.set_ylabel('Calories consumed')

# plt.plot(data.keys(), data.values(), color='#2B709F', marker="o")
# plt.axhline(y=2000, color="#C23737", ls="--")
# plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000])

# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)

# plt.savefig("calorie_plot.png")
# plt.show() TODO: uncomment
####
# print('snooze')
# d = [1,2,3,4]
# f = [data[date]] # TODO: figure out
f = [25, 15, 20, 5]

data2 = {
	'Left': 0 if data['05/29'] > 2001 else 2000 - data['05/29'], 
	# 'Consumed':data['05/29']
	'Left': 0 if data[date] > 2001 else 2000 - data[date], 
	'Consumed':data[date]
}

fig = plt.figure()
fig.set_size_inches(50,10)
ax1 = fig.add_subplot(221)
plt.barh(list(data2.keys()), data2.values(), edgecolor='white', color=['#196F3D', '#58D68D'])
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

# data2 = {'Week':14000}
ax2 = fig.add_subplot(222)

# line1 = ax2.plot(f,marker='.',color='#1B4F72',label="1 row")
ax2.set_xlabel('Date')
ax2.set_ylabel('Calories consumed')

plt.plot(data.keys(), data.values(), color='#2B709F', marker="o")
plt.axhline(y=2000, color="#C23737", ls="--")
plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000])
plt.xticks(rotation=30)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

grand_total, actual_total = len(data.keys()) * 2000, sum(data.values())
# actual_total = sum(data.values())

print('Actual total: ', actual_total, '\ngrand_total: ', grand_total, '\nProgress %: ', actual_total / grand_total * 100)

ax3 = fig.add_subplot(223)
ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
plt.bar(['Actual Count'], [actual_total])

plt.savefig("calorie_plot.png")
plt.show()