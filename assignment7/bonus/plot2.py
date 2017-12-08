import os
from matplotlib import pyplot as plt
import numpy as np

filename = 'steps.npy'

if os.path.exists(filename):
    data = np.load(filename)
    lmda = 0.90
    d = np.mean(data,axis=0)
    plt.plot(np.arange(1,d.shape[0]+1),d,label='Modified'.format(lmda))
    
    if os.path.exists('../part1and2/steps.npy'):
        data2 = np.load('../part1and2/steps.npy')
        d = np.mean(data2,axis=0)
        plt.plot(np.arange(1,d.shape[0]+1),d,label='Unmodified')
    
    
    plt.ylim([100,500])
    plt.xlabel('Episode')
    plt.ylabel('Steps per episode \naveraged over {} runs'.format(data.shape[0]))
    plt.legend()
    plt.savefig("bonus2.png")
    # plt.show()
