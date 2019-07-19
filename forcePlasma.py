# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 12:03:18 2018

@author: ruloz
"""

import numpy as np
import matplotlib.pyplot as plt

v = np.arange(4,21,1)
Fb = (1/10**10) * (v*1e3)**2.7893
Fb2 = 3.26 * v - 17.32
U = 0.000166 * v**3.5;

#----------------------Velocity plot------------------------------------------
plt.figure(1, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#plt.subplot(2, 1, 1)
plt.plot(v,U,':*',c='blueviolet',linewidth=1,markersize=4)
# add text labels to the plot
plt.legend(['Velocidad'])
plt.xlabel('Voltaje (kV)')
plt.ylabel('U (m/s)')
plt.title('Velocidad vs Voltaje')
plt.grid(True)
#plt.savefig('U_Volt.png')
# show the figure on the screen
plt.show()

#----------------------Force plot------------------------------------------
plt.figure(2, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#plt.subplot(2, 1, 1)
plt.plot(v,Fb,'--^',c='darkcyan',linewidth=1,markersize=4)
plt.plot(v,Fb2,'-.o',c='lime',linewidth=1,markersize=4)
# add text labels to the plot
plt.legend(['Potencial','Lineal'])
plt.xlabel('Voltaje (kV)')
plt.ylabel('F (mN/m)')
plt.title('Fuerza vs Voltaje')
plt.grid(True)
#plt.savefig('F_Volt.png')
# show the figure on the screen
plt.show()

k_v = 15
i = np.asscalar(np.argwhere(v == k_v))
U_kv = 0.000166 * k_v**3.5;
print( f'Velocidad = {U[i,]:.4f} m/s, Voltaje = {k_v} kV')
print( f'Fuerza por metro de plasma F = {Fb2[i,]:.4f} mN/m, Voltaje = {k_v} kV')
print( f'Fuerza por metro de plasma F = {Fb[i,]:.4f} mN/m, Voltaje = {k_v} kV')

U_infy = 3
dt = 0.0001
T = np.arange(0,1,dt)
f = 2e3
f_burst = 15 # 25 Hz, 100 Hz , 150 Hz
f_adi_base = f/U_infy
f_adi_burst = f_burst/U_infy

x = np.zeros((len(T),1),dtype=float)
y = np.zeros((len(T),1),dtype=float)
Ff = np.zeros((len(T),1),dtype=float)
for t in range(len(T)):
    x[t] = t*dt-dt
    Ff[t] = np.sign(np.sin(2*np.pi*f_burst*x[t]))
    if x[t]*Ff[t] > 0:
        y[t] = np.sin(2*np.pi*f*x[t])
    else:
        y[t] = 0
    
plt.figure(3, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
plt.plot(x,y,'--^',c='darkcyan',linewidth=1,markersize=1)
plt.legend(['$f_{base}$=  %a $Hz$ \n $F_{burst}$= %a $Hz$' %(f, f_burst)])
plt.xlabel('Tiempo (s)')
plt.ylabel('V')
plt.title('Ciclo de trabajo')
plt.grid(True)
#plt.savefig('f_burst_50.png')
plt.show()
print( f'Frecuencia base = {f} Hz, Frecuencia rafaga = {f_burst} Hz')
print( f'F_base^+ = {f_adi_base:.4f}, F_burst^+ = {f_adi_burst:.4f}')