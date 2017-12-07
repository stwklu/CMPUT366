#!/usr/bin/env python

"""
  Author: Adam White, Mohammad M. Ajallooeian, Sina Ghiassian
  Purpose: for use of Reinforcement learning course University of Alberta Fall 2017

"""

from utils import rand_norm, rand_in_range, rand_un
import numpy as np

current_state = None

def env_init():
    global current_state, start, num_total_states

def env_start():
    """ returns numpy array """
    global current_state

    x = np.random.uniform(-0.6,-0.4)
    current_state = np.array([x,0.0])

    return current_state

def env_step(action):
    """
    Arguments
    ---------
    action : int
        the action taken by the agent in the current state

    Returns
    -------
    result : dict
        dictionary with keys {reward, state, isTerminal} containing the results
        of the action taken
    """
    global current_state

    x,xdot = current_state

    #print "current state: {}".format(current_state)
    #print "action: {}".format(action)

    xdotp = bound_xdot(xdot+0.001*(action-1) - 0.0025*np.cos(3*x))
    xp = bound_x(x+xdotp)

    #print "xp: {} xdotp: {}".format(xp,xdotp)

    if xp == -1.2:
        xdotp = 0
    elif xp == 0.5:
        current_state = None
        return {'state':current_state,'reward':-1.0,'isTerminal':True}

    current_state = np.array([xp,xdotp])

    return {'state':current_state,"reward":-1.0,'isTerminal':False}

def bound_x(x):
    if x>0.5:
        return 0.5
    if x<-1.2:
        return -1.2
    return x

def bound_xdot(xdot):
    if xdot>0.07:
        return 0.07
    if xdot<-0.07:
        return -0.07
    return xdot


def env_cleanup():
    #
    return

def env_message(in_message): # returns string, in_message: string
    """
    Arguments
    ---------
    inMessage : string
        the message being passed

    Returns
    -------
    string : the response to the message
    """
    return ""
