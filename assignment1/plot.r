#!/usr/bin/env Rscript

# Author: Matthew Schlegel
# Purpose: Just a simple plotting util to read in data from RL_EXP_OUT.dat

dat = read.table("RL_EXP_OUT.dat")

plot(x = 1 : length(dat[, 1]), y = dat[,1], type = "l", ylab = "% Optimal Action", xlab = "Steps", col = "purple")
