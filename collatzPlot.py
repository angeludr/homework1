import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Collatz.txt')

Numbers = data['Number']
Steps = data['Steps']

plt.scatter(Numbers, Steps)

plt.savefig('Plot.png')

plt.show()
