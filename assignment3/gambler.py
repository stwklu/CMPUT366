#!/usr/bin/env python

import numpy as np

def value_iteration(values):
  delta = 0.0
  cutoff = 1**-6

  while delta > cutoff :
    for i in range (len(values)):
      v = values[i]
      values[i] = max_action()
      delta = max(delta, v - values[i])


def max_action():
  pass

def main():
  values = np.zeros(101)
  values[100] = 1.0

  value_iteration(values)

if __name__ == '__main__':
  main()