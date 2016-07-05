#!/usr/bin/env python
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
from random import shuffle

"""
Package to import normally distributed data for use

Data are retrieved from normal.pkl and normlist.pkl
    - made by norm_gen.py
"""
def load_normal(split):
    X = pickle.load(open("lib/normal.pkl","rb"))
    y = pickle.load(open("lib/normlist.pkl","rb"))
    zlist=list(zip(X,y))
    dataset = zlist
    shuffle(dataset)
    split_point = int(len(X) * split)
    xtrain_split = int(split_point + 0.5 * (1 - split) * len(X))
    return dataset[:split_point], dataset[split_point:xtrain_split], dataset[xtrain_split:]
