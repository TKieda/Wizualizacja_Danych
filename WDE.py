import sys
import numpy as np
import math
import random
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
##########Zestaw 24##############

#######ZAD 1########

x=[1,5,6,7,8,9,12,14,16,19,20,21,22,23,26,28,30]
y=[0.167,0.1675,0.1675,0.1678,0.1677,0.1674,0.1673,0.1683,0.1688,0.1689,0.1693,0.1687,0.1692,0.1691,0.1692,0.1697,0.1695]
fig, ax = plt.subplots(figsize=(7.2,5.4))
ax.plot(x,y,'r--')
ax.set(xticks=np.arange(0,35, 5),yticks=np.arange(0.165,0.170,0.001), title='Wykres w sierpniu 2019')
plt.text(29, 0.1685 ,'CZK',verticalalignment='baseline',horizontalalignment='right')
ax.grid()
plt.show()