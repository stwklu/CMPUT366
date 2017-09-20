# General Instructions
* Requires utils.py and rl_glue.py which are provided by the autograder.
* Using Python 2.7, execute `python w1_exp.py`
* Optimal Action Statistics are in RL_EXP_OUT.dat after running
* Parameters need to be manually altered in the code, see below.

# Parameters
## w1_agent.py
In order to change `alpha, epsilon, and q1`, please look near line ~25 in `w1_agent.py`. I have prepopulated the two requested parameter settings for ease of use.

# Random Seeding
Every single file (`w1_agent.py, w1_env.py, w1_exp.py`) uses only numpy for random and depends on the provided `utils.py`. In each of these files, the seed has been set to 123 via `np.random.seed(123)` in order to be able to replicate the "random" numbers generated between switching the parameters. In other words, this allows the two graphs to be compared as they operated on the same set of repeated data. Comment these three places out in order to re-introduce unseeded pseudorandom behavior.

# Plotting
1. Adjust parameters
    * See above
2. Run the experiment
    * `python w1_exp.py`
    * Data in `RL_EXP_OUT.dat` is overwritten
3. Plot using `rscript`
    * `./plot.r`
4. Rename the output PDF if desired or else overwritten next run. 
5. In order to print two experiments on the same graph, see comments in `plot.r`

# Data Files
As agent parameters must be changed in code as well as the output file name, the experiments must be ran sequentially which is fine due to the seeding and # of runs. However, this means that I have provided the data used to generate the corresponding plots (`w1_epsilongreedy.dat` and `w1_optimistic.dat`) as part of my submission.

In other words, the program does not run both experiments simultaneously, create two data files, and then two plots. One must run one experiment, and create the plot and then rename the data file and plot in order for them to not be overwritten by the second experiment.

