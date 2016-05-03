# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 04:58:34 2015

@author: anwar.maxsum
"""
# Pemodelan Kalman Filter
# Robot bergerak dengan kecepatan konstan
# X(t) = 1*X(t-1) + 0.05V + epsilon
# Z(t) = gps (Xt) + delta
# C  = 1
# delta = N (0, 0.01)
# epsilon = N (0,005)

import matplotlib.pyplot as mp
import numpy as np
# from scitools.std import *
	

def kalman_prediction (iteration, mu_prev, sigma_prev, ut, gpsY) :
    
    #inplementasikan kalman filter berdasarkan model
	#Prediction
	mu_bar = 1 * mu_prev + 0.05 * ut
	sigma_bar = 1 * sigma_prev * 1 + delta
	#Correction\
	Kt = sigma_t * 1 * 1/(1*sigma_t*1+0.01)
	mu_t = mu_bar + Kt * (gpsY - 1 * mu_bar)
	sigma_t = (1-Kt*1)*sigma_bar
	
    # plot x(t-1), z, dan x(t)
    figureName = 'iteration' + `iteration`
    mp.figure(figureName)
    #for mu, sig in [(mu_prev, sigma_prev), (gpsY, 0.001), (mu_t, sigma_t)]:
    for mu, sig in [(mu_bar, sigma_bar), (gpsY, 0.001), (mu_t, sigma_t)]:
    #for mu, sig in [(mu_prev, sigma_prev),(gpsY, 0.001)]:
        mp.plot(gaussian(np.linspace(-100.0, 100.0, 400), mu, sig))    
    mp.show()
         
    return [mu_t,sigma_t]
    

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / 2 * np.power(sig, 2.))
    
    

def plot(x, title):
    fig = mp.figure()
    ax = fig.add_subplot(111)
    
    ax.set_xlabel('robot position')
    ax.set_ylabel('bel(x)')
    fig.suptitle(title)
    
     
