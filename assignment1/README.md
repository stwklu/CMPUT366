**CMPUT366/609 - RLGlue README.md**
====================

Edited by: Mohammad M. Ajallooeian, Created on: Sep 15, 2017
Edited and modified from file by Matthew Schlegel, Jan 3, 2017, for use in
CMPUT 366/499/609.

This will be a general overview of the framework used for this course. It is a 
simpler version of the RLGlue found at 
http://glue.rl-community.org/wiki/Main_Page. 
Please use this for ALL assignment code unless otherwise specified in the 
assignment or in class. If there are any questions contact Adam White or 
Mohammad Ajallooeian.

You are required to use NumPy for storing vector/matrix data and 
highly encouraged to use NumPy for performing linear algebra operations and
calculations.

Running the experiment
---------------------

You should use Python 2.7+ to run experiments. Simply use:
python my_exp.py
in a Python 2 enabled environment to run an experiment file my_exp.py. 

Environment file : simple_env.py
---------------------

this contains a simple environment implementation and what you should base your
environments on during this class. There are several functions and variables
you should implement (**IMPORTANT**: Do NOT change the function names,
function input/output requirements, or RL Glue depnedencies in the code):

### env_init

The env_init function manages the initialization of the environment at the
beginning of the program. It is invoked during the RL_init(...) call. Any
environmental initializations happen here.

### env_start

The env_start function is called at the beginning of a run of the experiment. 
It is invoked during the RL_start function and should return the initial 
observation of the environment.

### env_step

This is the meat of the environment and where most of an experiment will take 
place. This should update the environment based on the given action, and return
a triple (r, o, t) where r is a floating point reward, o is a NumPy array 
representing the observation and t is a Boolean which is True only if the 
environment has reached a terminal state.

### env_cleanup

This function is called at the end of an experiment and should contain any 
cleaning up code neccessary.

### env_message

This function is used for sending messages from your experiment to your 
environment.


Agent file : simple_agent.py
---------------------

this contains a simple agent implementation and what you should base your 
agents on during this class. There are several functions and variables you 
should implement (**IMPORTANT**: Do NOT change the function names, function
input/output requirements, or RL Glue depnedencies in the code):

### agent_init

The agent_init function manages the initialization of the agent at the
beginning of the program. It is invoked during the RL_init(...) call. You
should do any agent initializations required outside a single experiment here.

### agent_start

The agent_start function is called at the beginning of a run of the experiment.
It is invoked after the environment makes its first observation during the
RL_start(...) function.
You should initialize what you need for a single experiment here.

This function also returns a NumPy array representing the next action to be
sent to the environment.

### agent_step

This is the meat of the agent and where most of the learning takes place. You
will implement various RL algorithms here.

This function also returns a NumPy array representing the next action to be
sent to the environment.

### agent_end

This function is called at the end.

### agent_cleanup

This function is called at the end of an experiment and should handle any
clean-ups neccessary.

### agent_message

This function is used for sending messages across your environment, agent and
experiment.

Experiment file : simple_exp.py
---------------------

Experiment file : simple_exp.py
---------------------

This file contains a basic RL experiment and will be executed to run the experiment.
**IMPORTANT**: Do NOT change RL Glue depnedencies.

Plotting: plot.r
--------------------

This is just an example plot file for R. Please feel free using any plotting
language you wish, but still include all code used for plotting.
