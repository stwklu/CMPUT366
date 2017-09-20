#!/usr/bin/env Rscript

# Author: Matthew Schlegel
# Purpose: Just a simple plotting util to read in data from RL_EXP_OUT.dat

dat = read.table("RL_EXP_OUT01.dat")

plot(x = 1 : length(dat[, 1]), y = dat[,1], type = "l", ylab = "% Optimal Action", xlab = "Steps", col = "purple", ylim=c(0,1))

dat = read.table("RL_EXP_OUT0.dat")

lines(x = 1 : length(dat[, 1]), y = dat[,1], type = "l", col = "red")
