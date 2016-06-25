#!/usr/local/bin/python

import numpy
from Image import Image

def main():
        #legend for diagnosis and input path and type of card
        print("1.Normal Conditions\n2.Gas Interference\n3.Fluid Pound\n4.Traveling Valve Leak\n5.Standing Valve Leak\n6.Pump Hitting on Top\n7.Pump Hitting on Bottom\n8.Plugged Pump Intake\n9.Flumping\n10.Gas Lock\n11.Tubing Movement or Malfunctions in Tubing anchor\n12.Rod Parted\n13.Oil Too viscous")
        Card_image = input("Enter card Path : ")
        Diagnosis = input("Enter Downhole Diagnosis index :")
        #save card descritpors into input file
        card= Image()
        descriptors=card.findDescriptor(Card_image)
        descriptors=card.truncate_descriptor(descriptors,18)
        print (descriptors)
        save = open("input.dat", "a")
       # numpy.savetxt(save,descriptors.view(complex).reshape(1, descriptors.shape[0]))
        numpy.savetxt(save, descriptors.reshape(1, descriptors.shape[0]), fmt = '%.4f%+.4fj '*18)
        numpy.save
        ##, fmt = "%.10f"
        save.close()
        #save card diagnosis into output file
        if Diagnosis ==1:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==2:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,0]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==3:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,1]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==4:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,2]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==5:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,3]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==6:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,4]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==7:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,5]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==8:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,6]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==9:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,7]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==10:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,8]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==11:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,9]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==12:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,10]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()
        elif Diagnosis ==13:
            save = open("output.dat", "a")
            output = numpy.zeros([1, 13], dtype=numpy.float32)
            output[0,11]=1
            numpy.savetxt(save, output.reshape(1, output.shape[1]), newline = "\r")
            save.close()

if __name__ == '__main__':
    main()
