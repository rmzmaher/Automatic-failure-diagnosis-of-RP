import numpy as np
import cPickle as pickle
import pylab as plt
import pyefd
import tkMessageBox

class NeuralNetwork:
    def predict(self,card):
        model_file = 'model.pkl'
        try:
            xs,y =  np.loadtxt(card+".txt", unpack=True)
        except Exception:
            tkMessageBox.showinfo("ERROR!","Error! Card you Entered is not Exist \n Please check file name")

        contour=[]
        i=0
        for x in xs:
            contour.append([x,y[i]])
            i=i+1
        coeffs = pyefd.elliptic_fourier_descriptors(contour, order=15,normalize=True)
        pyefd.plot_efd(coeffs)
        coeffs = coeffs.flatten()[1:]
        # load model
        net = pickle.load( open( model_file, 'rb' ))
        # predict
        p = net.activate(coeffs)
        #draw
        x = [1,2,3]
        LABELS = ["Normal", "Gas Interference", "Fluid Pound"]
        plt.bar(x, p, align='center')
        plt.xticks(x, LABELS)
        plt.show()
        ##########
        np.savetxt('predictions.txt', p, fmt = '%.6f' )