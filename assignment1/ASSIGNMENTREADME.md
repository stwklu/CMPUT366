# Parameters
## w1_agent.py
In order to change alpha, epsilon, and q1, please look near line ~25 in w1_agent.py. I have prepopulated the two requested parameter settings for ease of use.

# Random Seeding
Every single file (`w1_agent.py, w1_env.py, w1_exp.py`) uses only numpy for random and depends on the provided `utils.py`. In each of these files, the seed has been set to 123 via `np.random.seed(123)` in order to be able to replicate the "random" numbers generated between switching the parameters. In other words, this allows the two graphs to be compared as they operated on the same set of repeated data. Comment these three places out in order to re-introduce unseeded pseudorandom behavior.