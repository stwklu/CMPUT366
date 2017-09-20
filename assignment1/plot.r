#!/usr/bin/env Rscript

# Author: Matthew Schlegel
# Purpose: Just a simple plotting util to read in data from RL_EXP_OUT.dat

dat = read.table("RL_EXP_OUT.dat")

plot(x = 1 : length(dat[, 1]), y = dat[,1], type = "l", ylab = "% Optimal Action", xlab = "Steps", col = "purple", ylim=c(0,1))

# Uncomment below to plot two lines on the same graph. 
# Requires you to change the data file out name in w1_exp.py near the end
# dat = read.table("RL_EXP_OUT1.dat")

# lines(x = 1 : length(dat[, 1]), y = dat[,1], type = "l", col = "red")
