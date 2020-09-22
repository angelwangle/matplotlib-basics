# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:47:21 2020

@author: User
"""

import matplotlib.pyplot as pl
import numpy as np

x = np.linspace(-np.pi, np.pi, 256, endpoint = True)

y = np.cos(x)
y1 = np.sin(x)

pl.plot(x, y)
pl.plot(x, y1)

pl.show()