#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:22:40 2018

@author: anton
"""

import numpy as np
import matplotlib.pyplot as plt


def R0(t):
    return 1/t

def deformation(ksi1, ksi2, r0):
    
    alfa = (ksi1 - c)/L
    phi0 = (np.pi-L/r0)/2.
    
    phi = phi0+alfa*(np.pi - 2*phi0)
    r = r0 + ksi2 - a
    
    return r*np.cos(phi), r*np.sin(phi)-r0+a

def vel(ksi1, ksi2, r0, dr0):
    
    alfa = (ksi1 - c)/L
    phi0 = (np.pi-L/r0)/2.
    
    phi = phi0+alfa*(np.pi - 2*phi0)
    r = r0 + ksi2 - a
    
    return dr0*(np.cos(phi)-(1-2*alfa)/2*L*r*np.sin(phi)/r0/r0), dr0*(np.sin(phi)-1+(1-2*alfa)/2*L*r*np.cos(phi)/r0/r0)

def r0(t):
    return 1./t

def dr0(t):
    return -1./t/t

fig = plt.figure(figsize=(10,5))

ax2, ax1 = fig.add_subplot(1,2,1), fig.add_subplot(1,2,2)


t = np.linspace(0,1,num = 100)
a,b = 1., 1.5
c,d = -0.5, 0.5

L     = d-c
Delta = b-a

ksi1i = np.linspace(c,d, num = 100)
ksi2i = np.linspace(a,b, num = 100)

ksi1 = np.linspace(c,d, num = 7)
ksi2 = np.linspace(a,b, num = 5)

i = 0

for t in np.arange(0.01, 2, 0.05):

    # plt.tight_layout() 
    ax1.cla()  
    ax2.cla()

    # fig.suptitle("Деформация тела в лагранжевых и эйлеровых координатах t = %1.3f" % t)
    fig.suptitle("t = %1.2f" % t)
    # ax2.set_title("t = %1.3f" % t)

    ax1.grid(True)
    ax2.grid(True)

    ax1.set_xlabel('$x$')
    ax1.set_ylabel('$y$')

    ax1.set_xlim(-2*(b-a),2*(b-a))
    ax1.set_ylim((a+b)/2 - 2*(b-a), (a+b)/2+2*(b-a))
    
    
    ax2.set_xlabel('$\\xi_1$')
    ax2.set_ylabel('$\\xi_2$')

    ax2.set_xlim(-2*(b-a),2*(b-a))
    ax2.set_ylim((a+b)/2 - 2*(b-a), (a+b)/2+2*(b-a))
    
    
    for ksi in ksi2:
        x,y = deformation(ksi1i, np.array([ksi for x in ksi1i]), r0(t) )
        ax1.plot(x,y, 'b')
        
        ax2.plot(ksi1i, np.array([ksi for x in ksi1i]),'r')
        
    for ksi in ksi1:
        x,y = deformation(np.array([ksi for x in ksi2i]), ksi2i, r0(t) )
        ax1.plot(x,y, 'b')
        ax2.plot(np.array([ksi for x in ksi2i]), ksi2i,'r')

    for ksi10 in ksi1:
        for ksi20 in ksi2:

            xa,ya = deformation(ksi10, ksi20, r0(t) )
            vxa,vya = vel(ksi10, ksi20, r0(t), dr0(t)) 
        
            U,V = np.meshgrid(vxa, vya)
        
            q1 = ax1.quiver(xa, ya, U, V, width=0.004, scale=2)
            q2 = ax2.quiver(ksi10, ksi20, -U, V, width=0.004, scale=2)
            # ax.quiverkey(q, X=0.3, Y=1.1, U=10, label='Quiver key, length = 10', labelpos='E')
    
    plt.savefig("img/fig_%02d.pdf" % i, transparent=True)
    plt.pause(0.001)
    
    i+=1


   


# u,v = np.meshgrid(ksi1, ksi2)

# print(u)
  
# for ksi1t in ksi1:
#     for ksi2 in ksi2:
        



plt.show()