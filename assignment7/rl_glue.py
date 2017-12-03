#!/usr/bin/env python

"""
 Copyright (C) 2017, Adam White, Mohammad M. Ajallooeian


"""

from importlib import import_module

environment = None
agent = None

last_action = None # last_action: int
total_reward = None # total_reward: floating point
num_steps = None # num_steps: integer
num_episodes = None # num_episodes: integer

def RLGlue(env_name, agent_name):
    """
    Arguments
    ---------
    env_name : string
        filename of the environment module
    agent_name : string
        filename of the agent module
    """
    global environment, agent

    environment = import_module(env_name)
    agent = import_module(agent_name)

def RL_init():
    global total_reward, num_steps, num_episodes
    environment.env_init()
    agent.agent_init()

    total_reward = 0.0
    num_steps = 0
    num_episodes = 0

def RL_start():
    """
    Returns
    -------
    observation : dict
        dictionary containing what the first state and action were
    """
    global last_action, total_reward, num_steps
    total_reward = 0.0;
    num_steps = 1;

    last_state = environment.env_start()
    last_action = agent.agent_start(last_state)

    observation = {"state":last_state, "action":last_action}

    return observation

def RL_agent_start(state):
    """
    Arguments
    ---------
    state : numpy array
        the initial state the agent is starting in

    Returns
    -------
    int : the action taken by the agent
    """
    return agent.agent_start(state)

def RL_agent_step(reward,state):
    """
    Arguments
    ---------
    observation : dict
        a dictionary containing the reward and next state resulting from
        the agent's most-recent action

    Returns
    -------
    int : the action taken by the agent
    """
    return agent.agent_step(reward,state)

def RL_agent_end(reward):
    """
    Arguments
    ---------
    reward : float
        the final reward received by the agent
    """
    agent.agent_end(reward)

def RL_env_start():
    """
    Returns
    -------
    numpy array : the initial state
    """
    global total_reward, num_steps
    total_reward = 0.0
    num_steps = 1

    return environment.env_start()

def RL_env_step(action): # returns (floating point, NumPy array, Boolean), action: NumPy array
    """
    Arguments
    ---------
    action : int
        the most recent action taken by the agent

    Returns
    -------
    result : dict
        dictionary with keys {reward,state,isTerminal}
    """
    global total_reward, num_steps, num_episodes

    result = environment.env_step(action)

    total_reward += result['reward']

    if result['isTerminal'] == True:
        num_episodes += 1
    else:
        num_steps += 1

    return result

def RL_step():
    """
    Returns
    -------
    result : dict
        dictionary with keys {reward,state,action,isTerminal}
    """
    global last_action, total_reward, num_steps, num_episodes
    result = environment.env_step(last_action)
    total_reward += result['reward'];

    if result['isTerminal'] == True:
        num_episodes += 1
        agent.agent_end(result['reward'])
        result['action'] = None
    else:
        num_steps += 1
        last_action = agent.agent_step(result['reward'],result['state'])
        result['action'] = last_action

    return result

def RL_cleanup():
    environment.env_cleanup()
    agent.agent_cleanup()

def RL_agent_message(message):
    """
    Arguments
    ---------
    message : string
        the message to send to the agent

    Returns
    -------
    the_agent_response : string
        the agent's response to the message
    """
    if message is None:
        message_to_send = ""
    else:
        message_to_send = message

    the_agent_response = agent.agent_message(message_to_send)
    if the_agent_response is None:
        return ""

    return the_agent_response

def RL_env_message(message):
    """
    Arguments
    ---------
    message : string
        the message to send to the environment

    Returns
    -------
    the_env_response : string
        the environment's response to the message
    """
    if message is None:
        message_to_send = ""
    else:
        message_to_send = message

    the_env_response = environment.env_message(message_to_send)
    if the_env_response is None:
        return ""

    return the_env_response

def RL_episode(max_steps_this_episode):
    """
    Arguments
    ---------
    max_steps_this_episode : int

    Returns
    -------
    is_terminal : bool
    """
    is_terminal = False

    RL_start()
    while (not is_terminal) and ((max_steps_this_episode == 0) or (num_steps < max_steps_this_episode)):
        rl_step_result = RL_step()
        is_terminal = rl_step_result['isTerminal']

        # if (num_steps == (max_steps_this_episode)):
            # print 'not ended'

    return is_terminal


def RL_return():
    """ returns floating point """
    return total_reward

def RL_num_steps():
    """ returns integer """
    return num_steps

def RL_num_episodes():
    """ returns integer """
    return num_episodes
