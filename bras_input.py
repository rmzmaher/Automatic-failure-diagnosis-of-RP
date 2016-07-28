#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
========
Created by: ENG.Ramez Maher
Created on: 2016-07-02, 23:50
"""
import numpy as np
import matplotlib.pyplot as plt
import pyefd
import pandas as pd
#xx=np.arange(101) 
#yy=np.arange(101,202)
#legend for diagnosis and input path and type of card
print("1.Normal Conditions\n2.Gas Interference\n3.Fluid Pound\n4.Traveling Valve Leak\n5.Standing Valve Leak\n6.Pump Hitting on Top\n7.Pump Hitting on Bottom\n8.Plugged Pump Intake\n9.Flumping\n10.Gas Lock\n11.Tubing Movement or Malfunctions in Tubing anchor\n12.Rod Parted\n13.Oil Too viscous")
Cards = input("Enter cards File Name : ")
Diagnosis = input("Enter Downhole Diagnosis index :")
# x,y values for  cards
xx = pd.read_table('I:/Thesis - EFD/'+Cards+'.txt', delimiter=',', usecols=(np.arange(101) ), header=None)
yy = pd.read_table('I:/Thesis - EFD/'+Cards+'.txt', delimiter=',',usecols=(np.arange(101,202)), header=None)
xp = np.loadtxt("I:/Thesis - EFD/HittingUp,x3.txt", delimiter=',', usecols=(np.arange(101) ), unpack=True)
yp=np.loadtxt("I:/Thesis - EFD/HittingUp,x3.txt", delimiter=',', usecols=(np.arange(101,202)), unpack=True)
i=0
print(xp.shape)
for value in xx.values:
    contour=[]
    ii=0
    for x in value:
        y=yy.values[i]
        contour.append([x,y[ii]])
        ii=ii+1
    i=i+1
    coeffs = pyefd.elliptic_fourier_descriptors(contour, order=15,normalize=True)
    #pyefd.plot_efd(coeffs)
    coeffs=coeffs.flatten()[1:]
    save = open("input.dat", "a")
    np.savetxt(save, coeffs.reshape(1, coeffs.shape[0]))
# save card diagnosis into output file
    save2 = open("output.dat", "a")
    output = np.zeros([1, 3], dtype=np.float32)  
    if Diagnosis ==1:
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r")          
    elif Diagnosis ==2:
        output[0,0]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r")  
    elif Diagnosis ==3:
        output[0,1]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r")  
    elif Diagnosis ==4:
        output[0,2]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r")  
    elif Diagnosis ==5:
        output[0,3]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 
    elif Diagnosis ==6:
        output[0,4]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 
    elif Diagnosis ==7:
        output[0,5]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 
    elif Diagnosis ==8:
        output[0,6]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 
    elif Diagnosis ==9:
        output[0,7]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 
    elif Diagnosis ==10:
        output[0,8]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 
    elif Diagnosis ==11:
        output[0,9]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 
    elif Diagnosis ==12:
        output[0,10]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 
    elif Diagnosis ==13:
        output[0,11]=1
        np.savetxt(save2, output.reshape(1, output.shape[1]), newline = "\r") 

print (coeffs.shape)
plt.plot(xp, yp, linewidth=2.0)
plt.show()    
