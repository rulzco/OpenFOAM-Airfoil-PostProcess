#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 00:51:12 2018

@author: ruloz
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alfas = [0,4,8,12,13,14,15,16]
for a in alfas:
	theta = str(a)
	source_route = str('C:/Program Files/blueCFD-Core-2017/ofuser-of5/RANS/')
	df = pd.read_csv(source_route+'data/rans_'+theta+'.csv' )
	df2 = pd.read_csv(source_route+'data/rans1_'+theta+'.csv' )
	df3 = pd.read_csv(source_route+'data/rans2_'+theta+'.csv' )
	#print(df[0:3])

	t = 1.0
	u_infy = 3
	q = (0.5*u_infy**2)

	#------------------------Velocity RANS -------------------------------------------
	x = df['Points:0']
	Ux = df['U:0']
	Uy = df['U:0']
	Uz = df['U:2']
	U =  np.sqrt(np.power(Ux,2)+np.power(Uy,2)+np.power(Uz,2))
	#print(U[0:6])

	#------------------------Velocity RANS 0.1c--------------------------------------------
	x2 = df2['Points:0']
	Ux_2 = df2['U:0']
	Uy_2 = df2['U:0']
	Uz_2 = df2['U:2']
	U_2 = np.sqrt(np.power(Ux_2,2)+np.power(Uy_2,2)+np.power(Uz_2,2))

	#------------------------Velocity RANS 0.03c--------------------------------------------
	x3 = df3['Points:0']
	Ux_3 = df2['U:0']
	Uy_3 = df2['U:0']
	Uz_3 = df2['U:2']
	U_3 = np.sqrt(np.power(Ux_3,2)+np.power(Uy_3,2)+np.power(Uz_3,2))

	#------------------------Forces RANS 0.1c--------------------------------------------
	#df4 = pd.read_csv(source_route+theta+'pimple_alfa/postProcessing/forces/0/forceCoeffs.dat',sep='\t',comment='#')

	#Cl = df4.iloc[:,3]
	#Cd = df4.iloc[:,2]
	#Cm = df4.iloc[:,1]
	#time = df4.iloc[:,0]
	#------------------------Forces RANS 0.1c--------------------------------------------
	#df5 = pd.read_csv(source_route+theta+'pimple_alfa/postProcessing/residuals/0/residuals.dat',sep='\t',comment='#')

	#r_t = df5.iloc[:,0]                  
	#r_ux = df5.iloc[:,1]
	#r_uz = df5.iloc[:,2]
	#r_p = df5.iloc[:,3]
	#------------------------Data RANS ---------------------------------------------
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
	yPlus_rans = df['yPlus']
	#------------------------Data RANS 0.1c---------------------------------------------
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
	#print(cp_les[0:6])
	yPlus_1 = df2['yPlus']
	#------------------------Data RANS 0.03c---------------------------------------------
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
	#print(cp_les[0:6])
	yPlus_2 = df3['yPlus']
	#-----------------------Cp plot------------------------------------------------
	plt.figure(1, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,cp,'-o',c="blueviolet",markersize=5,markevery=20)
	plt.plot(x2,cp_1,':^',c="dodgerblue",markersize=5,markevery=20)
	plt.plot(x3,cp_2,'--s',c="k",markersize=5,markevery=20)
	#Actuator position line
	#plt.plot(np.array([0.75,0.75]),np.array([np.min(cp),np.max(cp)]),'--',linewidth=1)
	plt.gca().invert_yaxis()
	# add text labels to the plot
	#plt.legend(['Cp'])
	plt.legend(['$C_p$','$C_p$ ac $0.1c$','$C_p$ ac $0.03c$'])
	plt.xlabel('X (m)')
	plt.ylabel('Cp')
	plt.title('Cp vs X  %a°' %a)
	plt.grid(True)

	# save the figure as a PNG file 
	plt.savefig('figs/Cpx_rans_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#----------------------Vorticity plot------------------------------------------
	plt.figure(2, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,omega,'-o',c='coral',linewidth=1,markersize=5,markevery=20)
	plt.plot(x2,omega_1,':s',c="k",markersize=5,markevery=20)
	plt.plot(x3,omega_2,'-.>',c='mediumspringgreen',linewidth=1,markersize=5,markevery=20)
	#plt.plot(np.array([0.15,0.15]),np.array([np.min(omega_les),np.max(omega_les)]),'--2',linewidth=1,c='black')
	# add text labels to the plot
	plt.legend(['$\Omega$','$\Omega$ ac $0.1c$','$\Omega$ ac $0.03c$'])
	plt.xlabel('X (m)')
	plt.ylabel('Vorticidad')
	plt.title('Vorticidad vs %a°' %a)
	plt.grid(True)

	# save the figure as a PNG file 
	plt.savefig('figs/omega_rans_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#-----------------------Cf plot-----------------------------------------------
	plt.figure(3, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,cf,'-^',c='k',linewidth=1,markersize=5,markevery=20)
	plt.plot(x2,cf_1,'--d',c='dodgerblue',linewidth=1,markersize=5,markevery=20)
	plt.plot(x3,cf_2,'-.o',c='seagreen',linewidth=1,markersize=5,markevery=20)
	#plt.gca().invert_yaxis()
	# add text labels to the plot
	plt.legend(['$C_f$','$C_f$ ac $0.1c$','$C_f$ ac $0.03c$'])
	plt.xlabel('X (m)')
	plt.ylabel('Cf')
	plt.title('Cf vs X %a°' %a)
	plt.grid(True)

	# save the figure as a PNG file 
	plt.savefig('figs/Cfx_rans_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#---------------------yPlus plot-----------------------------------------------
	plt.figure(4, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(x,yPlus_rans,'-.o',c='seagreen',linewidth=1,markersize=5,markevery=20)
	#plt.plot(x,yPlus_les,':^',c="blueviolet",markersize=5,markevery=20)
	#plt.gca().invert_yaxis()
	# add text labels to the plot
	plt.legend(['$y^+$'])
	plt.xlabel('X (m)')
	plt.ylabel('$y^+$')
	plt.title('$y^+$ vs X %a°' %a)
	plt.grid(True)

	plt.savefig('figs/yPlus_rans_'+theta+'.png')
	# show the figure on the screen
	plt.show()

	#-----------------------Forces plot--------------------------------------------
	#plt.figure(5, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.plot(time,Cl,'-',c="lime",linewidth=1,markersize=2)
	#plt.plot(time,Cd*-1,'r:',linewidth=1,markersize=2)
	#plt.plot(time,Cm,'c--',linewidth=1,markersize=2)
	# add text labels to the plot
	#plt.legend(['Cl','Cd','Cm'])
	#plt.xlabel('Tiempo (s)')
	#plt.ylabel('Coeficientes')
	#plt.title('Coeficientes vs Tiempo %a°' %a)
	#plt.grid(True)
	#plt.savefig('figs/coeff_rans_'+theta+'.png')
	#plt.show()
	#-----------------------Residuals plot-----------------------------------------
	#plt.figure(6, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.semilogy(r_t,r_ux,'-',c="lime",linewidth=1,markersize=2)
	#plt.semilogy(r_t,r_uz,'-.',c='salmon',linewidth=1,markersize=2)
	#plt.semilogy(r_t,r_p,'--',c='darkcyan',linewidth=1,markersize=2)
	# add text labels to the plot
	#plt.legend(['Ux','Uz','P'])
	#plt.xlabel('Tiempo (s)')
	#plt.ylabel('Residuales')
	#plt.title('Residuales vs Tiempo %a°' %a)
	#plt.grid(True)
	#plt.savefig('figs/resi_rans_'+theta+'.png')
	#plt.show()
#------------------------Polars---------------------------------------------------
source_route = str('C:/Program Files/blueCFD-Core-2017/ofuser-of5/RANS/data/')
df6 = pd.read_csv(source_route+'polar.csv' )

#------------------------Coeffs RANS----------------------------------------------
alfa = df6['alfa']
Cl_r = df6['Cl:r']
Cd_r = df6['Cd:r']
Cm_r = df6['Cm:r']
#------------------------Coeffs 0.1C-----------------------------------------------
Cl_1 = df6['Cl:r1']
Cd_1 = df6['Cd:r1']
Cm_1 = df6['Cm:r1']
#-----------------------Coeffs 0.03------------------------------------------------
Cl_2 = df6['Cl:r2']
Cd_2 = df6['Cd:r2']
Cm_2 = df6['Cm:r2']
#-----------------------Cl plot---------------------------------------------------
plt.figure(7, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#plt.subplot(2, 1, 1)
plt.plot(alfa,Cl_r,'--s',c="turquoise",markersize=7)
plt.plot(alfa,Cl_1,'-.^',c="darkcyan",markersize=7)
plt.plot(alfa,Cl_2,'-d',c="salmon",markersize=7)
# add text labels to the plot
plt.legend(['$C_l$','$C_l$ ac $0.1c$','$C_l$ ac $0.03c$'])
plt.xlabel('$\\alpha$')
plt.ylabel('$C_l$')
plt.title('$C_l$ vs $\\alpha$')
plt.grid(True)

# save the figure as a PNG file 
plt.savefig('figs/Cl_rans_polar.png')
# show the figure on the screen
plt.show()
#-----------------------Cd plot---------------------------------------------------
plt.figure(8, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
#plt.subplot(2, 1, 1)
plt.plot(alfa,Cd_r,'-^',c="indianred",markersize=7)
plt.plot(alfa,Cd_1,':o',c="cornflowerblue",markersize=7)
plt.plot(alfa,Cd_2,'-.d',c="seagreen",markersize=7)
# add text labels to the plot
plt.legend(['$C_d$','$C_d$ ac $0.1c$','$C_d$ ac $0.03c$'])
plt.xlabel('$\\alpha$')
plt.ylabel('$C_d$')
plt.title('$C_d$ vs $\\alpha$')
plt.grid(True)

# save the figure as a PNG file 
plt.savefig('figs/Cd_rans_polar.png')
# show the figure on the screen
plt.show()
