#!/usr/bin/env python

import numpy as np

### PARAMETERS ###
# Probability of heads 
ph = 0.4
### PARAMETERS ###

def value_iteration(values, policy):
  delta = 100.0
  cutoff = 0.1

  # while delta > cutoff :
  for i in range (1,100):
    v = values[i]
    values[i] = max_action(values, policy, i)
    # print(v)
    # print(values)
    delta = max(delta, v - values[i])
    # print(delta)


def max_action(values, policy, i):
  v_kplus1 = 0.0
  max_value = 0.0

  # Try every action possible from current state i
  for action in range(0, i):
    # Does the action achieve our goal from our current state?
    if (i>98):
      print("act+i")
      print(action+i)
    if (action + i) >= 100:
      print("heeeeerrr")
      # Reward of 1.0 for reaching goal off of a heads
      v_kplus1 = (ph * (1.0 + values[i])) + ((1.0 - ph) * (0.0 + values[i])) 
    else:
      v_kplus1 = (ph * (0.0 + values[i])) + ((1.0 - ph) * (0.0 + values[i]))

    if v_kplus1 > max_value:
      max_value = v_kplus1
  
  return max_value

def main():
  values = np.zeros(101)
  values[100] = 1.0
  policy = np.zeros(101)

  value_iteration(values, policy)

  print(values)

if __name__ == '__main__':
  main()