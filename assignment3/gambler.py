#!/usr/bin/env python

import numpy as np

### PARAMETERS ###
# Probability of heads 
ph = 0.55
### PARAMETERS ###


def value_iteration(values, policy):
  theta = 10**-18
  delta = 999
  sweep = 0

  while delta > theta :
    sweep += 1
    delta = 0.0
    for state in range (1,100):
      v = values[state]
      values[state] = max_value(values, policy, state)
      delta = max(delta, abs(v - values[state]))

  print("Sweep Total = " + str(sweep))

def max_value(values, policy, state):
  v_kplus1 = 0.0 
  max_value = 0.0 # Best value for this round of actions on state
  best_action = 0

  # Try every action possible from current state i
  for action in range(0, min(state, 100 - state) + 1): # +1 because range ends one short

    v_kplus1 = (ph * (values[state + action])) + ((1.0 - ph) * (values[state - action]))

    # Python has issues comparing very similar floats
    # If similar, do not update
    if (v_kplus1 - max_value) < 10**-12:
      continue

    if v_kplus1 > max_value:
      max_value = v_kplus1
      best_action = action


  policy[state] = best_action

  return max_value


def main():
  values = [0.0] * 101
  values[100] = 1.0
  policy = [0] * 101

  value_iteration(values, policy)

  np.save("Value", values)
  np.save("Policy", policy)


if __name__ == '__main__':
  main()