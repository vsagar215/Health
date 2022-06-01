import matplotlib.pyplot as plt
import json

data = json.load(open("calorie_log.json", "r"))
f, ax = plt.subplots(figsize=(15,9))
ax.set_xlabel('Date')
ax.set_ylabel('Calories consumed')

plt.plot(data.keys(), data.values(), color='#2B709F', marker="o")
plt.axhline(y=2000, color="#566573", ls="--")
plt.yticks([0, 500, 1000, 1500, 2000, 2500, 3000])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.savefig("calorie_log.png")
plt.show()