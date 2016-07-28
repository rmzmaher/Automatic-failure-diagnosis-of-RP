#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests.py
========
Created by: ENG.Ramez Maher
Created on: 2016-07-02, 23:50
"""
import numpy as np
import matplotlib.pyplot as plt
import pyefd
import os.path

#legend for diagnosis and input path and type of card
print("1.Normal Conditions\n2.Gas Interference\n3.Fluid Pound\n4.Traveling Valve Leak\n5.Standing Valve Leak\n6.Pump Hitting on Top\n7.Pump Hitting on Bottom\n8.Plugged Pump Intake\n9.Flumping\n10.Gas Lock\n11.Tubing Movement or Malfunctions in Tubing anchor\n12.Rod Parted\n13.Oil Too viscous")
#Cards = input("Enter cards File Name : ")
Diagnosis = input("Enter Downhole Diagnosis index :")
# x,y values for  cards
i=1
while (os.path.isfile("I:\Thesis - EFD\leak_standing\ls"+str(i)+".txt") ):
#get x,y and plot all cards
    x,y =  np.loadtxt("I:\Thesis - EFD\leak_standing\ls"+str(i)+".txt", unpack=True)
    plt.plot(x, y)
    i=i+1
    ii=0
    contour=[]
    for xval in x:
        contour.append([xval,y[ii]])
        ii=ii+1
    coeffs = pyefd.elliptic_fourier_descriptors(contour, order=15,normalize=True)
    pyefd.plot_efd(coeffs)
    coeffs=coeffs.flatten()[3:]
    save = open("input.dat", "a")
    np.savetxt(save, coeffs.reshape(1, coeffs.shape[0]))
    np.save
# save card diagnosis into output file
    save2 = open("output.dat", "a")
    output = np.zeros([1, 13], dtype=np.float32)  
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
        
plt.show()