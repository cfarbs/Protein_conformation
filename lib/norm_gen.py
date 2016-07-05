#!/usr/bin/env python
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

"""
Script for generating values for use with a two-layer neural network

Generation of random normally distributed data
    -Randomly generates three means and and standard deviations from
    non-overlapping distributions.
    -Uses generated means and sds to pull 500 values from each distribution
    -Pickles the values into normal.pkl.
Generation of labels for data
    -creates list containing 500 of each 0, 1, and 2 (1500 values total)
    -Pickles into normlist.pkl.
"""


RNG = np.random.RandomState()


meanA = np.random.uniform(-5,-4)
meanB = np.random.uniform(4,5)
meanC = np.random.uniform(-1,1)

sdA = np.random.uniform(0,1)
sdB = np.random.uniform(0,1)
sdC = np.random.uniform(0,1)

samples=[]

Asamples=[0] * 500
#print (len(Asamples))
Bsamples=[1] * 500
Csamples=[2] * 500

loclist=Asamples + Bsamples + Csamples
pickle.dump(loclist,open("normlist.pkl","wb"))
#print (loclist)

for line in range(500):
    Ax=np.random.normal(loc=meanA,scale=sdA)
    Ay=np.random.normal(loc=meanA,scale=sdA)
    A = (Ax,Ay)
    samples.append(A)
    #pickle.dump(samples,open("normal.pkl","wb"))

for line in range(500):
    Bx=np.random.normal(loc=meanB,scale=sdB)
    By=np.random.normal(loc=meanB,scale=sdB)
    B = (Bx,By)
    samples.append(B)
    #pickle.dump(samples,open("normal.pkl","wb"))

for line in range(500):
    Cx=np.random.normal(loc=meanC,scale=sdC)
    Cy=np.random.normal(loc=meanC,scale=sdC)
    C = (Cx,Cy)
    samples.append(C)

pickle.dump(samples,open("normal.pkl","wb"))
data=pickle.load(open("normal.pkl","rb"))
locallist=pickle.load(open("normlist.pkl","rb"))
#print (len(data))
#print(type(data[5]))
#print(data[5].shape)
#zlist = list(zip(data,locallist))
#print (zlist[1001])
#x_val = [x[0] for x in data]
#y_val = [x[1] for x in data]
#plt.plot(x_val,y_val)
#plt.show()
