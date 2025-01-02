x = 2
y = [1,2,4,6,1.1,1.5,5,1.95,9,3]

for i in range(len(y)):
    if x <= i:
        print(f'this number {x},is less than y')
    else:
        print('number is ok')

import matplotlib.pyplot as plt
from matplotlib import style
import math
from math import sqrt

style.use ('ggplot')

import numpy as np

x_new = np.linspace(0,100,2)
y_new = np.cos(x_new)

plt.bar(x_new,y_new)
plt.show()

