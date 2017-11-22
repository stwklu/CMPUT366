# Main Readme
## How to Run
`python random_walk_exp.py`

## State Aggregation
While the assignment suggests using alpha = 0.1, I found the resulting error graph to be quite erratic, bumpy, high variability. Further, the result was an aggressive drop between states 0-50. When comparing this to Figure 9.10 in the text, I experimented with lowering alpha. With alpha = 0.01, the resulting graph is much smoother and more closely resembles that in the textbook. The sacrifice is the quick reduction in RMSE. A quick 5 run averaged graph is available as `random_walk01.png`.

Further, I implemented state aggregation both in a "manual" sense (see `old_aggregation_agent.py`) by mapping state to one of ten indices, similar to the tabular case. I found this to be very noisy when graphing. Instead, the `aggregation_agent.py` uses `tiles3.py` with one tiling layer and achieves superior results. The main graph `random_walk.png` uses this method. 
# Polynomials
## Deciding on level of polynomial/exponent

All agents used alpha = 0.001 for now. The agent name refers to the maximum exponent computed. For example, `polynomial3_agent` uses the feature vector (s^0, s^1, s^2, s^3) where s is the state input divided by 1000. The source code to rerun these experiments is included. Modify the agents around line 22 to be ran in `random_walk_exp.py` and then run `python random_walk_exp.py`. The resulting graph (`polynomial.png`) reveals that only considering (s^0, s^1) performs noticeable worse than the higher dimension polynomial implementations. As the polynomial order increases (EG `polynomial4`), RMSE drops faster initially (see around 1000 episodes) but by 5000 episodes, `polynomial2` has the lowest error and the higher the polynomial, the more error. ie, higher polynomials learn quicker initially but underperform given extra time. Therefore, I will be selecting `polynomial2_agent` to be the basis of my alpha tuning in the next experiment.

## Deciding on level of alpha
Starting off of `polynomial2`, I will test a variety of alpha levels and graph results. The number coming after `polynomial2` in the agent name refers to the alpha level. EG: `polynomial2001` runs a feature vector of (s^0, s^1, s^2) and alpha = 0.01. I tested alphas of 0.1, 0.01, and 0.001 and produced the graph `polynomialalphav1.png`. 0.1 was far too large, resulting in massive amount of noise and variability. No useful learning. 0.001 was too small, not learning quickly enough though was nice and smooth. 0.01 reduced error fairly quick while remaining calm enough. Some tuning to 0.01 could be done.

Next I tried just above and below alpha = 0.01 with 0.03 and 0.003 respectively. Again, all code and files are provided. Modify agents in `random_walk_exp.py` to repeat. The resulting graph is `polynomialalphav2.png`. Both 0.003 and 0.01 resulted in similar error beyond 3000 episodes. 0.03 was still quite noisy. Figure 9.5 demonstrates a low noise graph, and therefore I have opted to keep alpha = 0.003, though 0.01 is a close contender.

## Summary
 From the above testing, I found that using a polynomial feature vector of (state^0, state^1, state^2) and alpha of 0.003 to be the optimal selection for this problem. This agent (`polynomial20003`) alone will be graphed with the three required agents on one graph.