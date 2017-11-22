# Main Readme
## How to Run
`python random_walk_exp.py`
## Random Walk Environment (Part 1)
Part 1 is accomplished in `random_walk_env.py`
## Three Agents (Part 2)
The three requested agents can be found in:
* `tabular_agent.py`
* `tile_coding_agent.py`
* `aggregation_agent.py`
### State Aggregation Info and Explanations 
While the assignment suggests using alpha = 0.1, I found the resulting error graph to be quite erratic, bumpy, high variability. Further, the result was an aggressive drop between states 0-50. When comparing this to Figure 9.10 in the text, I experimented with lowering alpha. With alpha = 0.01, the resulting graph is much smoother and more closely resembles that in the textbook. The sacrifice is the quick reduction in RMSE. A quick 5 run, 3000 episode averaged graph is available as `random_walk01.png`.

Further, I implemented state aggregation both in a "manual" sense (see `old_aggregation_agent.py`) by mapping state to one of ten indices, similar to the tabular case. I found this to be very noisy when graphing. Instead, the `aggregation_agent.py` uses `tiles3.py` with one tiling layer and achieves superior results. The main graph `random_walk.png` uses this method. 

## Requested Plot (Part 3)
Look at `random_walk.png` for the requested graph that covers Part 3 and the bonus plotting requirements. For the sake of completeness, the three agent only graph (as requested in Part 3) without the bonus can be found at `random_walk_no_bonus.png`. RMSE is calculated in `random_walk_exp.py`. All graphs mentioned here (ie, the required graphs) are 5000 episodes long, and averaged over 10 runs. Other non-required graphs usually note reduced run numbers to save on compute time as they are simply assisting in a demo.
## Miscellaneous
* The random seed is controlled as requested. See `random_walk_exp.py`. The same run number in any agent will have the same seed set at its start.
* I use `rndmwalk_policy_evaluation.py` to get my true values for calculating RMSE. These are saved to `TrueValueFunction.npy`. If that file is deleted, the experiment will regenerate the true values, so long as the `rndmwalk_policy_evaluation.py` file is available. All are included in my upload. 

# Polynomials (Bonus)
## Deciding on level of polynomial/exponent

All agents used alpha = 0.001 for now. The agent name refers to the maximum exponent computed. For example, `polynomial3_agent` uses the feature vector (s^0, s^1, s^2, s^3) where s is the state input divided by 1000. The source code to rerun these experiments is included. Modify the agents around line 22 to be ran in `random_walk_exp.py` and then run `python random_walk_exp.py`. The resulting graph (`polynomial.png`) reveals that only considering (s^0, s^1) performs noticeable worse than the higher dimension polynomial implementations. As the polynomial order increases (EG `polynomial4`), RMSE drops faster initially (see around 1000 episodes) but by 5000 episodes, `polynomial2` has the lowest error and the higher the polynomial, the more error. ie, higher polynomials learn quicker initially but underperform given extra time. Therefore, I will be selecting `polynomial2_agent` to be the basis of my alpha tuning in the next experiment.

## Deciding on level of alpha
Starting off of `polynomial2`, I will test a variety of alpha levels and graph results. The number coming after `polynomial2` in the agent name refers to the alpha level. EG: `polynomial2001` runs a feature vector of (s^0, s^1, s^2) and alpha = 0.01. I tested alphas of 0.1, 0.01, and 0.001 and produced the graph `polynomialalphav1.png`. 0.1 was far too large, resulting in massive amount of noise and variability. No useful learning. 0.001 was too small, not learning quickly enough though was nice and smooth. 0.01 reduced error fairly quick while remaining calm enough. Some tuning to 0.01 could be done.

Next I tried just above and below alpha = 0.01 with 0.03 and 0.003 respectively. Again, all code and files are provided. Modify agents in `random_walk_exp.py` to repeat. The resulting graph is `polynomialalphav2.png`. Both 0.003 and 0.01 resulted in similar error beyond 3000 episodes. 0.03 was still quite noisy. Figure 9.5 demonstrates a low noise graph, and therefore I have opted to keep alpha = 0.003, though 0.01 is a close contender.

## Summary and Discussion
 From the above testing, I found that using a polynomial feature vector of (state^0, state^1, state^2) and alpha of 0.003 to be the optimal selection for this problem. This agent (`polynomial20003`) alone will be graphed with the three required agents on one graph.

 Viewing the final resulting graph `random_walk.png`, the polynomial agent does have lower RMSE than the aggregation agent at 5000 episodes. However, for the first half of 5000 episodes, polynomial is the slowest in reducing RMSE. Unfortunately, with only 5000 episodes, we cannot see how polynomial will trend, as polynomial is not leveled off as much as the other three agents. In general, I do not believe polynomial to be a great agent choice for this problem. We are dealing with a a single input to define our space. A problem that deals with two or more inputs to state (say, length and width, or age and weight), these inputs can have meaningful combinations. EG Area, BMI, etc. Having state^2, or state^3 is simply making features for the sake of features. Still, perhaps the machine will surprise us and find good features that I do not currently see. That being said, we did not see much difference for state^2 and higher polynomial combinations. Therefore, those higher order implementations do not improve, and can also hinder, the performance. This is supported in `polynomial.png`. 