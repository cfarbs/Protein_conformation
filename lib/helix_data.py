#!/usr/bin/env python
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from random import shuffle

"""
Package to import helix data for use

Data are retrieved from len=12_helices.pkl and len=12_rand.pkl

"""
def load_helix(split):
    X = pickle.load(open("lib/helices.pkl","rb"))
    y = pickle.load(open("lib/randhelices.pkl","rb"))
    dataset = X + y
    shuffle(dataset)
    split_point = int(len(X) * split)
    xtrain_split = int(split_point + 0.5 * (1 - split) * len(X))
    return dataset[:split_point], dataset[split_point:xtrain_split], dataset[xtrain_split:]
