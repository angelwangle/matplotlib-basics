# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:53:40 2020

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

mu = 100
sigma = 15
x = np.random.normal(mu, sigma, 10000)
ax = plt.gca()

# the histogram of the data
ax.hist(x, bins = 35, color = 'r')

ax.set_xlabel('Values')
ax.set_ylabel('Frequency')

ax.set_title(r'$\mathrm{Histogram:}\ \mu = %d,\ \sigma = %d$' % (mu, sigma))

plt.show()

