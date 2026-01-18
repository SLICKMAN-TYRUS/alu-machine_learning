#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# your code here
people = ['Farrah', 'Fred', 'Felicia']
width = 0.5
x = np.arange(len(people))

# Plot stacked bars
plt.bar(x, fruit[0], width, color='red', label='apples')
plt.bar(x, fruit[1], width, bottom=fruit[0], color='yellow', label='bananas')
plt.bar(x, fruit[2], width, bottom=fruit[0] + fruit[1],
        color='#ff8000', label='oranges')
plt.bar(x, fruit[3], width, bottom=fruit[0] + fruit[1] + fruit[2],
        color='#ffe5b4', label='peaches')

plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.xticks(x, people)
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))
plt.legend()
plt.show()
