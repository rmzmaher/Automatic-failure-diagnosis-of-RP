import numpy as np
import cPickle as pickle
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets            import ClassificationDataSet
from pybrain.structure.modules import SoftmaxLayer
from pybrain.utilities import percentError



output_model_file = 'model.pkl'

hidden_size = 50
epochs = 50
continue_epochs = 10	
validation_proportion = 0.15
# load data

x_train = np.loadtxt("input.dat", delimiter = ' ')
print x_train.shape

y_train = np.loadtxt( "output.dat", delimiter = ' ' )
print y_train.shape

input_size = x_train.shape[1]
target_size = y_train.shape[1]

# prepare dataset

ds = ClassificationDataSet( input_size, target_size,nb_classes=3 )
ds.setField( 'input', x_train )
ds.setField( 'target', y_train )

tstdata, trndata = ds.splitWithProportion( 0.25 )

# init and train

net = buildNetwork( input_size, hidden_size, target_size,outclass=SoftmaxLayer)
trainer = BackpropTrainer( net,dataset=trndata, learningrate=0.01 ,verbose=True,weightdecay=.01 )
print "training for {} epochs...".format( epochs )

trainer.trainUntilConvergence( verbose = True, validationProportion = validation_proportion, maxEpochs = epochs, continueEpochs = continue_epochs )
trnresult = percentError(trainer.testOnClassData(),trndata['target'])
tstresult = percentError(trainer.testOnClassData(dataset=tstdata), tstdata['target'])

print("epoch: %4d" % trainer.totalepochs,
              "  train error: %5.2f%%" % trnresult,
              "  test error: %5.2f%%" % tstresult)
    
pickle.dump( net, open( output_model_file, 'wb' ))
