#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 00:51:12 2018

@author: ruloz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alfas = [16]
for a in alfas:
	theta = str(a)
	source_route = str('C:/Program Files/blueCFD-Core-2017/ofuser-of5/RANS/')
	df = pd.read_csv(source_route+'data/smago_'+theta+'.csv' )
	df2 = pd.read_csv(source_route+'data/smago_r1_'+theta+'.csv' )
	df3 = pd.read_csv(source_route+'data/smago_r2_'+theta+'.csv' )
	df4 = pd.read_csv(source_route+'data/rans1_'+theta+'.csv' )
	df5 = pd.read_csv(source_route+'data/rans2_'+theta+'.csv' )
	#print(df[0:3])

	t = 1.0
	u_infy = 3
	q = (0.5*u_infy**2)

	#------------------------Velocity LES-------------------------------------------
	x = df['Points:0']
	Ux = df['U:0']
	Uy = df['U:0']
	Uz = df['U:2']
	U =  np.sqrt(np.power(Ux,2)+np.power(Uy,2)+np.power(Uz,2))
	#print(U[0:6])

	#------------------------Velocity LES 0.1c --------------------------------------------
	Ux_2 = df2['U:0']
	Uy_2 = df2['U:0']
	Uz_2 = df2['U:2']
	U_2 = np.sqrt(np.power(Ux_2,2)+np.power(Uy_2,2)+np.power(Uz_2,2))

	#------------------------Velocity LES 0.03c--------------------------------------------
	x3 = df3['Points:0']
	Ux_3 = df3['U:0']
	Uy_3 = df3['U:0']
	Uz_3 = df3['U:2']
	U_3 = np.sqrt(np.power(Ux_3,2)+np.power(Uy_3,2)+np.power(Uz_3,2))

	#------------------------Velocity RANS 0.1c--------------------------------------------
	x4 = df4['Points:0']
	Ux_4 = df4['U:0']
	Uy_4 = df4['U:0']
	Uz_4 = df4['U:2']
	U_4 = np.sqrt(np.power(Ux_4,2)+np.power(Uy_4,2)+np.power(Uz_4,2))
    
    #------------------------Velocity RANS 0.03c--------------------------------------------
	x5 = df5['Points:0']
	Ux_5 = df5['U:0']
	Uy_5 = df5['U:0']
	Uz_5 = df5['U:2']
	U_5 = np.sqrt(np.power(Ux_5,2)+np.power(Uy_5,2)+np.power(Uz_5,2))

	#------------------------Data LES ---------------------------------------------
	tau_x = df['wallShearStress:0']
	tau_y = df['wallShearStress:1']
	tau_z = df['wallShearStress:2']
	tau = np.sqrt(np.power(tau_x,2)+np.power(tau_y,2)+np.power(tau_z,2))
	cf = tau/q

	omega_x = df['vorticity:0']
	omega_y = df['vorticity:1']
	omega_z = df['vorticity:2']
	omega = np.sqrt(np.power(omega_x,2)+np.power(omega_y,2)+np.power(omega_z,2))
	#print(omega[0:6])

	cp = df['p']/q
	#print(cp[0:6])
	yp_1 = df['yPlus']
	yPlusMean1 = yp_1.mean()
	#------------------------Data LES 0.1c---------------------------------------------
	tau_x1 = df2['wallShearStress:0']
	tau_y1 = df2['wallShearStress:1']
	tau_z1 = df2['wallShearStress:2']
	tau_1 = np.sqrt(np.power(tau_x1,2)+np.power(tau_y1,2)+np.power(tau_z1,2))
	cf_1 = tau_1/q

	omega_x1 = df2['vorticity:0']
	omega_y1 = df2['vorticity:1']
	omega_z1 = df2['vorticity:2']
	omega_1 = np.sqrt(np.power(omega_x1,2)+np.power(omega_y1,2)+np.power(omega_z1,2))

	cp_1 = df2['p']/q
	yp_2 = df2['yPlus']
	yPlusMean2 = yp_2.mean()
	#------------------------Data LES 0.03c---------------------------------------------
	tau_x2 = df3['wallShearStress:0']
	tau_y2 = df3['wallShearStress:1']
	tau_z2 = df3['wallShearStress:2']
	tau_2 = np.sqrt(np.power(tau_x2,2)+np.power(tau_y2,2)+np.power(tau_z2,2))
	cf_2 = tau_2/q

	omega_x2 = df3['vorticity:0']
	omega_y2 = df3['vorticity:1']
	omega_z2 = df3['vorticity:2']
	omega_2 = np.sqrt(np.power(omega_x2,2)+np.power(omega_y2,2)+np.power(omega_z2,2))

	cp_2 = df3['p']/q
	yp_3 = df3['yPlus']
	yPlusMean3 = yp_3.mean()
    #------------------------Data RANS 0.1c---------------------------------------------
	tau_x3 = df4['wallShearStress:0']
	tau_y3 = df4['wallShearStress:1']
	tau_z3 = df4['wallShearStress:2']
	tau_3 = np.sqrt(np.power(tau_x3,2)+np.power(tau_y3,2)+np.power(tau_z3,2))
	cf_3 = tau_3/q

	omega_x3 = df4['vorticity:0']
	omega_y3 = df4['vorticity:1']
	omega_z3 = df4['vorticity:2']
	omega_3 = np.sqrt(np.power(omega_x3,2)+np.power(omega_y3,2)+np.power(omega_z3,2))

	cp_3 = df4['p']/q
	yp_4 = df4['yPlus']
	yPlusMean4 = yp_4.mean()
    #------------------------Data RANS 0.03c---------------------------------------------
	tau_x4 = df5['wallShearStress:0']
	tau_y4 = df5['wallShearStress:1']
	tau_z4 = df5['wallShearStress:2']
	tau_4 = np.sqrt(np.power(tau_x4,2)+np.power(tau_y4,2)+np.power(tau_z4,2))
	cf_4 = tau_4/q

	omega_x4 = df5['vorticity:0']
	omega_y4 = df5['vorticity:1']
	omega_z4 = df5['vorticity:2']
	omega_4 = np.sqrt(np.power(omega_x4,2)+np.power(omega_y4,2)+np.power(omega_z4,2))

	cp_4 = df5['p']/q
	yp_5 = df5['yPlus']
	yPlusMean5 = yp_5.mean()
	#-----------------------Cp plot------------------------------------------------
	plt.figure(1, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,cp,'-o',c="blueviolet",markersize=5,markevery=20)
	plt.plot(x,cp_1,':^',c="dodgerblue",markersize=5,markevery=20)
	plt.plot(x3,cp_2,'--s',c="k",markersize=5,markevery=20)
	plt.plot(x4,cp_3,'+',c="red",markersize=7,markevery=10)
	plt.plot(x5,cp_4,'*',c="seagreen",markersize=5,markevery=10)
	#Actuator position line
	#plt.plot(np.array([0.75,0.75]),np.array([np.min(cp),np.max(cp)]),'--',linewidth=1)
	plt.gca().invert_yaxis()
	# add text labels to the plot
	#plt.legend(['Cp'])
	plt.legend(['$C_p$ Smagorinsky','$C_p$ Smagorinsky ac $0.1c$','$C_p$ Smagorinsky ac $0.03c$','$C_p$ $k-\Omega$ 0.1c','$C_p$ $k-\Omega$ 0.03c'])
	plt.xlabel('X (m)')
	plt.ylabel('Cp')
	plt.title('Cp vs X  %a°' %a)
	plt.grid(True)

	# save the figure as a PNG file 
	plt.savefig('RANS/figs/LES/Cpx_sma_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#----------------------Vorticity plot------------------------------------------
	plt.figure(2, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,omega,'-o',c='coral',linewidth=1,markersize=5,markevery=20)
	plt.plot(x,omega_1,':s',c="k",markersize=5,markevery=20)
	plt.plot(x3,omega_2,'-.>',c='mediumspringgreen',linewidth=1,markersize=5,markevery=20)
	plt.plot(x4,omega_3,':+',c="red",markersize=7,markevery=15)
	plt.plot(x5,omega_4,':*',c="navy",markersize=5,markevery=15)
	#plt.plot(np.array([0.15,0.15]),np.array([np.min(omega_les),np.max(omega_les)]),'--2',linewidth=1,c='black')
	# add text labels to the plot
	plt.legend(['$\Omega$ Smagorinsky','$\Omega$ Smagorinsky ac $0.1c$','$\Omega$ Smagorinsky ac $0.03c$','$\Omega$ RANS 0.1c','$\Omega$ RANS 0.03c'])
	plt.xlabel('X (m)')
	plt.ylabel('Vorticidad')
	plt.title('Vorticidad vs %a°' %a)
	plt.grid(True)

	# save the figure as a PNG file 
	plt.savefig('RANS/figs/LES/omega_sma_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#-----------------------Cf plot-----------------------------------------------
	plt.figure(3, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,cf,'-^',c='k',linewidth=1,markersize=5,markevery=20)
	plt.plot(x,cf_1,'--d',c='dodgerblue',linewidth=1,markersize=5,markevery=20)
	plt.plot(x3,cf_2,'-.o',c='seagreen',linewidth=1,markersize=5,markevery=20)
	plt.plot(x4,cf_3,'+',c="red",markersize=7,markevery=20)
	plt.plot(x5,cf_4,'*',c="navy",markersize=5,markevery=20)
	#plt.gca().invert_yaxis()
	# add text labels to the plot
	plt.legend(['$C_f$ Smagorinsky','$C_f$ Smagorinsky ac $0.1c$','$C_f$ Smagorinsky ac $0.03c$','$C_f$ $k-\Omega$ SST 0.1c','$C_f$ $k-\Omega$ SST 0.03c'])
	plt.xlabel('X (m)')
	plt.ylabel('Cf')
	plt.title('Cf vs X %a°' %a)
	plt.grid(True)

	# save the figure as a PNG file 
	plt.savefig('RANS/figs/LES/Cfx_sma_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#---------------------yPlus plot-----------------------------------------------
	plt.figure(4, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,yp_1,'-.o',c='seagreen',linewidth=1,markersize=5,markevery=20)
	#plt.plot(x,yp_2,'-.o',c='seagreen',linewidth=1,markersize=5,markevery=20)
	#plt.plot(x3,yp_3,':^',c="blueviolet",markersize=5,markevery=20)
	#plt.gca().invert_yaxis()
	# add text labels to the plot
	plt.legend(['$y^+$'])
	plt.xlabel('X (m)')
	plt.ylabel('$y^+$')
	plt.title('$y^+$ vs X %a°' %a)
	plt.grid(True)

	plt.savefig('RANS/figs/LES/yPlus_les_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	print( f'y+ promedio  = {yPlusMean1:.4f} malla 1 {theta}°')
	print( f'y+ promedio  = {yPlusMean2:.4f} malla 2 {theta}°')
	print( f'y+ promedio  = {yPlusMean3:.4f} malla 3 {theta}°')    