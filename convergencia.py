# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:17:26 2019

@author: ruloz
"""

#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 00:51:12 2018

@author: ruloz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alfas = [0,4,8,12,16]
for a in alfas:
	theta = str(a)
	source_route = str('C:/Program Files/blueCFD-Core-2017/ofuser-of5/')
	df = pd.read_csv(source_route+'data/malla1r_'+theta+'.csv' )
	df2 = pd.read_csv(source_route+'data/malla2r_'+theta+'.csv' )
	df3 = pd.read_csv(source_route+'data/malla3r_'+theta+'.csv')
	df4 = pd.read_csv(source_route+'data/16_3d.csv')
	#print(df[0:3])
    
	t = 1.0
	u_infy = 3
	q = (0.5*u_infy**2)
	x = df['Points:0']
	x2 = df2['Points:0']
	x3 = df3['Points:0']
	x4 = df4[['Points:0']]
	#------------------------Velocity Malla1--------------------------------------------
	
	Ux_1 = df['U:0']
	Uy_1 = df['U:0']
	Uz_1 = df['U:2']
	U_1 = np.sqrt(np.power(Ux_1,2)+np.power(Uy_1,2)+np.power(Uz_1,2))
	#print(U[0:6])

	#------------------------Velocity Malla2---------------------------------------------
	Ux_2 = df2['U:0']
	Uy_2 = df2['U:0']
	Uz_2 = df2['U:2']
	U_2 = np.sqrt(np.power(Ux_2,2)+np.power(Uy_2,2)+np.power(Uz_2,2))
    
    #------------------------Velocity Malla3---------------------------------------------
	Ux_3 = df3['U:0']
	Uy_3 = df3['U:0']
	Uz_3 = df3['U:2']
	U_3 = np.sqrt(np.power(Ux_3,2)+np.power(Uy_3,2)+np.power(Uz_3,2))
    
    #------------------------Velocity MallaLES---------------------------------------------
	Ux_4 = df4['U:0']
	Uy_4 = df4['U:0']
	Uz_4 = df4['U:2']
	U_4 = np.sqrt(np.power(Ux_4,2)+np.power(Uy_4,2)+np.power(Uz_4,2))

	#------------------------Data Malla1---------------------------------------------
	tau_x1 = df['wallShearStress:0']
	tau_y1 = df['wallShearStress:1']
	tau_z1 = df['wallShearStress:2']
	tau1 = np.sqrt(np.power(tau_x1,2)+np.power(tau_y1,2)+np.power(tau_z1,2))
	cf_1 = tau1/q

	omega_x1 = df['vorticity:0']
	omega_y1 = df['vorticity:1']
	omega_z1 = df['vorticity:2']
	omega_1 = np.sqrt(np.power(omega_x1,2)+np.power(omega_y1,2)+np.power(omega_z1,2))
	#print(omega[0:6])

	cp_1 = df['p']/q
	#print(cp[0:6])
    
	yp_1 = df['yPlus']
	yPlusMean1 = yp_1.mean()
	#------------------------Data Malla2----------------------------------------------
	tau_x2 = df2['wallShearStress:0']
	tau_y2 = df2['wallShearStress:1']
	tau_z2 = df2['wallShearStress:2']
	tau_2 = np.sqrt(np.power(tau_x2,2)+np.power(tau_y2,2)+np.power(tau_z2,2))
	cf_2 = tau_2/q

	omega_x2 = df2['vorticity:0']
	omega_y2 = df2['vorticity:1']
	omega_z2 = df2['vorticity:2']
	omega_2 = np.sqrt(np.power(omega_x2,2)+np.power(omega_y2,2)+np.power(omega_z2,2))

	cp_2 = df2['p']/q
	#print(cp_les[0:6])
	yp_2 = df2['yPlus']
	yPlusMean2 = yp_2.mean()
	#------------------------Data Malla3-----------------------------------------------
	tau_x3 = df3['wallShearStress:0']
	tau_y3 = df3['wallShearStress:1']
	tau_z3 = df3['wallShearStress:2']
	tau_3 = np.sqrt(np.power(tau_x3,2)+np.power(tau_y3,2)+np.power(tau_z3,2))
	cf_3 = tau_3/q

	omega_x3 = df3['vorticity:0']
	omega_y3 = df3['vorticity:1']
	omega_z3 = df3['vorticity:2']
	omega_3 = np.sqrt(np.power(omega_x3,2)+np.power(omega_y3,2)+np.power(omega_z3,2))

	cp_3 = df3['p']/q
	#print(cp_les[0:6])
	yp_3 = df3['yPlus']
	yPlusMean3 = yp_3.mean()
    #------------------------Data MallaLES-----------------------------------------------
	tau_x4 = df3['wallShearStress:0']
	tau_y4 = df3['wallShearStress:1']
	tau_z4 = df3['wallShearStress:2']
	tau_4 = np.sqrt(np.power(tau_x4,2)+np.power(tau_y4,2)+np.power(tau_z4,2))
	cf_4 = tau_3/q

	omega_x4 = df4['vorticity:0']
	omega_y4 = df4['vorticity:1']
	omega_z4 = df4['vorticity:2']
	omega_4 = np.sqrt(np.power(omega_x4,2)+np.power(omega_y4,2)+np.power(omega_z4,2))

	cp_4 = df4['p']/q
	#print(cp_les[0:6])
	yp_4 = df4['yPlus']
	yPlusMean4 = yp_4.mean()
	#-----------------------Cp plot------------------------------------------------
	plt.figure(1, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,cp_1,':o',c="blueviolet",markersize=7,markevery=20)
	plt.plot(x2,cp_2,':^',c="steelblue",markersize=7,markevery=20)
	plt.plot(x3,cp_3,'-.s',c="k",markersize=5,markevery=20)
	#Actuator position line
	#plt.plot(np.array([0.75,0.75]),np.array([np.min(cp),np.max(cp)]),'--',linewidth=1)
	plt.gca().invert_yaxis()
	# add text labels to the plot
	#plt.legend(['Cp'])
	plt.legend(['Cp Malla 1','Cp Malla 2','Cp Malla 3'])
	plt.xlabel('X (m)')
	plt.ylabel('Cp')
	plt.title('Cp vs X  %a°' %a)
	plt.grid(True)
	# save the figure as a PNG file 
	plt.savefig('figs/ac/Cp_conv_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#----------------------Vorticity plot------------------------------------------
	plt.figure(2, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,omega_1,':o',c='coral',linewidth=1,markersize=5,markevery=20)
	plt.plot(x2,omega_2,'->',c='mediumspringgreen',linewidth=1,markersize=5,markevery=20)
	plt.plot(x3,omega_3,'--s',c="k",markersize=5,markevery=20)
	#plt.plot(np.array([0.15,0.15]),np.array([np.min(omega_les),np.max(omega_les)]),'--2',linewidth=1,c='black')
	# add text labels to the plot
	plt.legend(['$\Omega$ Malla 1','$\Omega$ Malla 2','$\Omega$ Malla 3'])
	plt.xlabel('X (m)')
	plt.ylabel('Vorticidad')
	plt.title('Vorticidad vs X %a°' %a)
	plt.grid(True)
	# save the figure as a PNG file 
	plt.savefig('figs/ac/omega_conv_'+theta+'.png')
	# show the figure on the screen
	plt.show()
	#-----------------------Cf plot-----------------------------------------------
	plt.figure(3, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,cf_1,'-.^',c='palegreen',linewidth=1,markersize=5,markevery=20)
	plt.plot(x2,cf_2,'c--d',linewidth=1,markersize=5,markevery=20)
	plt.plot(x3,cf_3,'-.s',c="k",markersize=5,markevery=20)
	#plt.gca().invert_yaxis()
	# add text labels to the plot
	plt.legend(['Cf Malla 1','Cf Malla 2','Cf Malla 3'])
	plt.xlabel('X (m)')
	plt.ylabel('Cf')
	plt.title('Cf vs X %a°' %a)
	plt.grid(True)
	# save the figure as a PNG file 
	plt.savefig('figs/ac/Cfx_conv_'+theta+'.png')
	# show the figure on the screen
	plt.show()
    
    #----------------------yPlus plot---------------------------------------------
	plt.figure(3, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,yp_1,'-.^',c='palegreen',linewidth=1,markersize=5,markevery=20)
	plt.plot(x2,yp_2,'c--d',linewidth=1,markersize=5,markevery=20)
	plt.plot(x3,yp_3,'-.s',c="k",markersize=5,markevery=20)
	#plt.gca().invert_yaxis()
	# add text labels to the plot
	plt.legend(['$y^+$ Malla 1','$y^+$ Malla 2','$y^+$ Malla 3'])
	plt.xlabel('X (m)')
	plt.ylabel('$y^+$')
	plt.title('$y^+$ vs x %a°' %a)
	plt.grid(True)
	# save the figure as a PNG file 
	plt.savefig('figs/ac/yplus_conv_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#-----------------------Cp plotLES------------------------------------------------
	plt.figure(1, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x3,cp_3,':^',c="steelblue",markersize=7,markevery=20)
	plt.plot(x4,cp_4,'-.s',c="k",markersize=5,markevery=20)
	#Actuator position line
	#plt.plot(np.array([0.75,0.75]),np.array([np.min(cp),np.max(cp)]),'--',linewidth=1)
	plt.gca().invert_yaxis()
	# add text labels to the plot
	#plt.legend(['Cp'])
	plt.legend(['Cp Malla 3','Cp Malla 3D'])
	plt.xlabel('X (m)')
	plt.ylabel('Cp')
	plt.title('Cp vs X  %a°' %a)
	plt.grid(True)
	# save the figure as a PNG file 
	plt.savefig('figs/ac/Cp_conv_LES_16.png')
	# show the figure on the screen
	plt.show()
    
	print( f'y+ promedio  = {yPlusMean1:.4f} malla 1 {theta}°')
	print( f'y+ promedio  = {yPlusMean2:.4f} malla 2 {theta}°')
	print( f'y+ promedio  = {yPlusMean3:.4f} malla 3 {theta}°')    
    
#------------------------Polars---------------------------------------------------
source_route = str('C:/Program Files/blueCFD-Core-2017/ofuser-of5/data/')
df6 = pd.read_csv(source_route+'convergencia_malla.csv' )

#------------------------Coeffs Malla1-----------------------------------------------
alfa = df6['alfa']
Cl_1 = df6['Cl:1']
Cd_1 = df6['Cd:1']
Cm_1 = df6['Cm:1']
#------------------------Coeffs Malla2-----------------------------------------------
Cl_2 = df6['Cl:2']
Cd_2 = df6['Cd:2']
Cm_2 = df6['Cm:2']
#-----------------------Coeffs Malla3--------------------------------------------
Cl_3 = df6['Cl:3']
Cd_3 = df6['Cd:3']
Cm_3 = df6['Cm:3']
#-----------------------Cl plot---------------------------------------------------
plt.figure(6, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#plt.subplot(2, 1, 1)
plt.plot(alfa,Cl_1,'-s',c="salmon",markersize=8)
plt.plot(alfa,Cl_2,'-.^',c="seagreen",markersize=7)
plt.plot(alfa,Cl_3,'--d',c="dodgerblue",markersize=7)
# add text labels to the plot
plt.legend(['Cl Malla 1','Cl Malla 2','Cl Malla 3'])
plt.xlabel('$\\alpha$')
plt.ylabel('Cl')
plt.title('Cl vs $\\alpha$')
plt.grid(True)
# save the figure as a PNG file 
plt.savefig('figs/ac/Cl_polarConv.png')
# show the figure on the screen
plt.show()
#-----------------------Cd plot---------------------------------------------------
plt.figure(7, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#plt.subplot(2, 1, 1)
plt.plot(alfa,Cd_1,'-^',c="indianred",markersize=9)
plt.plot(alfa,Cd_2,':o',c="cornflowerblue",markersize=7)
plt.plot(alfa,Cd_3,'-.d',c="seagreen",markersize=7)
plt.legend(['Cd Malla 1','Cd Malla 2','Cd Malla 3'])
plt.xlabel('$\\alpha$')
plt.ylabel('Cd')
plt.title('Cd vs $\\alpha$')
plt.grid(True)
# save the figure as a PNG file 
plt.savefig('figs/ac/Cd_polarConv.png')
# show the figure on the screen
plt.show()

