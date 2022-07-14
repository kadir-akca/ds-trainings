from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

hour = range(24)
viewer = [34, 7, 2, 8, 10, 81, 7, 0, 44, 66, 77, 34, 23, 12, 76, 8, 9, 45, 23, 43, 56, 78, 45, 34]
date = '10.03.2022'

plt.title('Viewers pro hours')

plt.xlabel('Hour')
plt.ylabel('Viewers')

plt.plot(hour, viewer)

plt.legend([date])

ax = plt.subplot()

ax.set_facecolor('yellow')

ax.set_xticks(hour)
ax.set_yticks([0, 15, 30, 45, 60, 75, 90])

y_upper = [i + (i*0.15) for i in viewer]
y_lower = [i - (i*0.15) for i in viewer]

plt.fill_between(hour, y_lower, y_upper, alpha=0.5, step='post')

plt.show()