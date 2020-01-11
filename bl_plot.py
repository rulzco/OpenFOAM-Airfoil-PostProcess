"""
Created on Mon Jun 17 19:31:41 2019

@author: ruloz
"""

#!/usr/bin/python3

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alfas2 = [12]
for a in alfas2:
	theta2 = str(a)
	#------------------------Boundary Layer------------------------------------------------
	source_route = str('C:/Program Files/blueCFD-Core-2017/ofuser-of5/RANS/data/')
	df = pd.read_csv(source_route+'bl_'+theta2+'.csv' )
	df2 = pd.read_csv(source_route+'bl_r1_'+theta2+'.csv' )
	df3 = pd.read_csv(source_route+'bl_r2_'+theta2+'.csv' )
	#------------------------BL RANS DATA--------------------------------------------------
	arc_l1 = df['arc_length']
	ux= df['U:0']
	uy = df['U:1']
	uz= df['U:2']
	U = np.sqrt(np.power(ux,2)+np.power(uy,2)+np.power(uz,2))
	#------------------------BL RANS DATA 1--------------------------------------------------
	arc_l2 = df2['arc_length']
	ux_r1 = df2['U:0']
	uy_r1 = df2['U:1']
	uz_r1= df2['U:2']
	U_r1 = np.sqrt(np.power(ux_r1,2)+np.power(uy_r1,2)+np.power(uz_r1,2))
	#------------------------BL RANS DATA 2--------------------------------------------------
	arc_l3 = df3['arc_length']
	ux_r2 = df3['U:0']
	uy_r2 = df3['U:1']
	uz_r2= df3['U:2']
	U_r2 = np.sqrt(np.power(ux_r2,2)+np.power(uy_r2,2)+np.power(uz_r2,2))

	#-----------------------BL plot------------------------------------------------
	plt.figure(8, figsize=(8, 6), dpi=90, facecolor='w', edgecolor='w')
	#plt.subplot(2, 1, 1)
	plt.plot(U,arc_l1,'--o',c="indianred",markersize=6,markevery=30)
	plt.plot(U_r1,arc_l2,'-.^',c="seagreen",markersize=6,markevery=30)
	plt.plot(U_r2,arc_l3,':s',c="blueviolet",markersize=6,markevery=30)
	# add text labels to the plot
	plt.legend(['No ac','ac 0.1x/c','ac 0.03x/c'])
	plt.xlabel('U (m/s)')
	plt.ylabel('$\Delta z$ (m)')
	plt.title('Capa límite %a°' %a)
	plt.grid(True)
	# save the figure as a PNG file 
	plt.savefig('figs/BL_les_'+theta2+'.png')
	# show the figure on the screen
	plt.show()