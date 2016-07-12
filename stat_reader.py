#!/usr/bin/env python
import pickle
import numpy as np
import matplotlib.pyplot as plt

results = pickle.load(open("helix_modelssummary_stats.pkl","rb"))
epochs = np.arange(0,1000,100)
#print (results.keys())

plt.plot(epochs, results['train_accuracies'])
plt.plot(epochs, results['xtrain_accuracies'])

plt.legend(['Training Accuracies', 'Xtrain Accuracies'], loc = 'upper left')

plt.show()
