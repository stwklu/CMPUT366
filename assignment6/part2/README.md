# Polynomials
## Deciding on level of polynomial/exponent

All agents used alpha = 0.001 for now. The agent name refers to the maximum exponent computed. For example, `polynomial3_agent` uses the feature vector (s^0, s^1, s^2, s^3) where s is the state input divided by 1000. The source code to rerun these experiments is included. Modify the agents around line 22 to be ran in `random_walk_exp.py` and then run `python random_walk_exp.py`. The resulting graph (`polynomial.png`) reveals that only considering (s^0, s^1) performs noticeable worse than the higher dimension polynomial implementations. As the polynomial order increases (EG `polynomial4`), RMSE drops faster initially (see around 1000 episodes) but by 5000 episodes, `polynomial2` has the lowest error and the higher the polynomial, the more error. ie, higher polynomials learn quicker initially but underperform given extra time. Therefore, I will be selecting `polynomial2_agent` to be the basis of my alpha tuning in the next experiment.

## Deciding on level of alpha
