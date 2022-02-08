# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 16:29:57 2020

@author: ejonnst
"""

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

print("I like ", np.pi)

face = misc.face()
plt.imshow(face)
plt.show()
