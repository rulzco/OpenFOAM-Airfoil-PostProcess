# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:15:34 2018

@author: ruloz
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
#from mpl_toolkits.mplot3d import Axes3D

#Sadegh Aberouman Model conditions
freq = 10e3
D = 1e-5
V_0 = 15e3#10.5 409N/m^3
E = 2.8

#Kloker Model conditions
x_pa = 0.0
a0 = 55
a1 = 8
a2 = 10 
b0 = 34
b1 = 2.7
b2 = 0.7
cx = 80
rho_0 = 1.225
u_0 = 34.922
L = 0.04
magF = (rho_0*u_0**2)/L
#---------------------Domain and Mesh------------------------------------------
nx = 300
ny = 300
xmin = 0; xmax = 0.007
ymin = 0; ymax = 0.004
dx = (xmax-xmin)/(nx-1)
dy = (ymax-ymin)/(ny-1)
x = np.linspace(0,xmax,nx)
y = np.linspace(0,ymax,ny)
X,Y = np.meshgrid(x,y)
fx = np.empty([nx,ny])

#---------------------Model functions------------------------------------------

def modelSadegh(X,Y,nx,ny,freq,D,V_0,E,fx):

    a = (3.1054*freq**0.5*E**(0.01411)*D**-0.5*((-9.405e-11)*V_0**3 +  
     (5.918e-6)*V_0**2 + (-0.008657)*V_0 + 17.9))*1e-2
    b = ((0.0069e-3)*(V_0-30e3)-0.1)*1e6
    c = ((0.069e-3)*(V_0-30e3)-1.5)*1e3                             
    
    
    for i in range(nx):
       for j in range (ny):
            fx[i,j] = a*X[i,j]*E**(b*X[i,j]**2+c*Y[i,j])
            f_Sadegh = fx
    return f_Sadegh
            

def modelKloker(X,Y,nx,ny,fx,x_pa,a0,a1,a2,b0,b1,b2,cx,magF):
    fx = np.empty([nx,ny])
    for i in range(nx):
        for j in range (ny):
            fx[i,j] = cx*(a0*a1*X[i,j]+a0**2*a2*X[i,j]**2)*np.exp(-a0*X[i,j])*\
            (b1*Y[i,j]+b2*Y[i,j]**2)*np.exp(-b0*Y[i,j]**(2/5))
    f_Kloker = magF*np.rot90(fx)
    return f_Kloker

mu = 1e-5
sigma = 0.5
gx = np.exp(-(x-mu)**2/(2*sigma**2))

plt.figure(1, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
plt.plot(x,gx,':',c="blueviolet",markersize=2)
#plt.plot(x,cp_les,':',c="cyan",markersize=2)

#-------------------Plot Sadegh Aberoumand Model-------------------------------
F_Sadegh = modelSadegh(X,Y,nx,ny,freq,D,V_0,E,fx)
plt.figure(2, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#CS = plt.contour(X, Y, fx,linewidth=0.05,colors='k')
#plt.clabel(CS, inline=1, colors='w', fontsize=7)
CS = plt.pcolor(X,Y,F_Sadegh,cmap='jet')
plt.axes().set_aspect('equal')
#plt.legend(['Potencial','Lineal'])
plt.xlabel('x (m)')
plt.ylabel('z (m)')
plt.title('Fuerza de cuerpo $\\frac{N}{m^3}$')
ax = plt.gca()
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(CS, cax=cax)

maxForce = np.max(F_Sadegh)
print(f'Fuerza máxima = {maxForce:.4f} N/m^3 Modelo Sadegh')

#-------------------Plot Kloker Model-------------------------------
F_Kloker = modelKloker(X,Y,nx,ny,fx,x_pa,a0,a1,a2,b0,b1,b2,cx,magF)
plt.figure(3, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#CS = plt.contour(X, Y, fx,linewidth=0.05,colors='k')
#plt.clabel(CS, inline=1, colors='w', fontsize=7)
CS = plt.pcolor(X,Y,F_Kloker,cmap='jet')
plt.axes().set_aspect('equal')
#plt.legend(['Potencial','Lineal'])
plt.xlabel('x (m)')
plt.ylabel('z (m)')
plt.title('Fuerza de cuerpo $\\frac{N}{m^3}$')
ax = plt.gca()
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(CS, cax=cax)

maxForce = np.max(F_Kloker)
print(f'Fuerza máxima = {maxForce:.4f} N/m^3 Modelo Kloker')

#plt.figure(3, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#fig = plt.figure()
#ax = plt.axes(projection='3d')
#ax.plot_surface(x, y, fx, cmap=plt.cm.jet, rstride=1, cstride=1, linewidth=0)
#ax.view_init(0, 90)
#plt.show()

