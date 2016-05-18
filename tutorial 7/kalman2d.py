# -*- coding: utf-8 -*-
"""
Created on Fri May 13 08:12:29 2016

@author: Arshad
"""

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.mlab import bivariate_normal
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def kalman_prediction_2d (iteration, mu_prev, sigma_prev, ut, zt) :
    
   '''
   Implementasi di bagian ini.
   '''
    #Prediction
   At = np.matrix(((1,0,1,0),(0,1,0,1),(0,0,1,0),(0,0,0,1)))
   Bt = np.matrix(((0.5,0),(0,0.5),(1,0),(0,1)))
   Ct = np.matrix(((1,0,0,0),(0,1,0,0)))
   Ex = np.matrix(((0.25,0,0.5,0),(0,0.25,0,0.5),(0.5,0,1,0),(0,0.5,0,1)))
   Ez = np.matrix(((0.25,0),(0,0.25)))
   I = np.matrix(((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)))
   
   mu_bar = At * mu_prev + Bt * ut
   sigma_bar = At * sigma_prev * At.transpose() + Ex
   #Correction\
   Kt = sigma_bar * Ct.transpose() * 1/(Ct*sigma_bar*Ct.transpose() +Ez)
   mu_t = mu_bar + Kt * (zt - Ct * mu_bar)
   sigma_t = (I-Kt*Ct)*sigma_bar   
   
   zt_plot = np.array([[zt[0,0]],[zt[1,0]],[0],[0]])
   plot_update(iteration, mu_prev, sigma_prev, zt_plot, meas_noise, mu_t, sigma_t)
   
   
   return [mu_t,sigma_t]


def plot_update(i, mu_prev, sigma_prev, zt, sigma_zt, mu_t, sigma_t):
    X = np.linspace(-2.5, 2.5, 60)
    Y = np.linspace(-2.5, 2.5, 60)
    X, Y = np.meshgrid(X, Y)
  
    mu_prev_plot = np.array([[mu_prev[0,0]],[mu_prev[1,0]]])
    sigma_prev_plot = np.array([[sigma_prev[0,0],0],[0,sigma_prev[1,1]]])

    zt_plot = np.array([zt[0,0],zt[1,0]])
    sigma_zt = np.array([[sigma_zt[0,0],0],[0,sigma_zt[1,1]]])
    
    mu_t_plot = np.array([mu_t[0,0],mu_t[1,0]])
    sigma_t_plot = np.array([[sigma_t[0,0],0],[0,sigma_t[1,1]]])
    
    Z_prev = pdf_2dgauss(X,Y,mu_prev_plot,sigma_prev_plot)
    Z_zt = pdf_2dgauss(X,Y,zt_plot,sigma_zt)
    Z_t = pdf_2dgauss(X,Y,mu_t_plot,sigma_t_plot)
    
    fig = plt.figure('iteration' + `i`)
    ax = fig.gca(projection='3d')
    
    #surf_zt = ax.plot_surface(X, Y, Z_zt, rstride=1, cstride=1, cmap=cm.terrain, linewidth=0, antialiased=False)
    surf_prev = ax.plot_surface(X, Y, Z_prev, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    
    surf_t = ax.plot_surface(X, Y, Z_t, rstride=1, cstride=1, cmap=cm.PiYG, linewidth=0, antialiased=False)
 
    ax.set_zlim(0, 0.5)                   
    ax.zaxis.set_major_locator(LinearLocator(5))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    
    fig.colorbar(surf_prev, shrink=0.5, aspect=5)
    #fig.colorbar(surf_zt, shrink=0.5, aspect=5)
    fig.colorbar(surf_t, shrink=0.5, aspect=5)
    
    plt.title('State Estimation')
            
    plt.show()
    
        
    
def pdf_2dgauss (X, Y, mu, sigma):
    return bivariate_normal(X, Y,
                                 np.sqrt(sigma[ 0 ][ 0 ]),
                                 np.sqrt(sigma[ 1 ][ 1 ]),
                                 mu[0], mu[1],
                                 sigma[ 0 ][ 1 ])
                                 

                  

                  
                  
                  
                  
                  
                  
                  
                  
                  
#print(Rt)