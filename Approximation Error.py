# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SAjxXDLXKKZnfj8eF6ZsTvpLtsFfNyxN
"""

import matplotlib.pyplot as plt
import numpy as np


xold = float(50)

def F(x):
  return (x**3) - x - 1

def Fprime(x):
  return 3*(x**2) - 1


epsilon = 1e-10

temp1 = []
temp2 = []

itr = 1

while F(xold) > epsilon:
  up = F(xold)
  down = Fprime(xold)
  div = up/down
  xnew = xold - div
  ae = abs( xnew-xold )
  rae = ae/xnew
  temp1.append(ae)
  temp2.append(itr)
  print( xold, up, down, xnew, ae, rae )
  itr = itr+1

  xold = xnew

x = np.array(temp2)
y = np.array(temp1)

plt.bar(x,y)
plt.show()