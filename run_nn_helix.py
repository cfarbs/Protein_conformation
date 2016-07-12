#!/usr/bin/env python

import sys
import pickle
from lib.neural_network import classify_with_network3, classify_with_network2
from argparse import ArgumentParser
from multiprocessing import Process, current_process, Manager

def parse_args():
    parser = ArgumentParser(description=__doc__)

    #query files
    parser.add_argument('--group_1','-1',action = 'store',
                        dest = 'group_1', required=True, type=str,
                        default=None,help="group 1 files")
    parser.add_argument('--group_2', '-2', action='store',
                        dest='group_2', required=True, type=str, default=None,
                        help="group 2 files")
    parser.add_argument('--group_3', '-3', action='store',
                        dest='group_3', required=False, type=str, default=None,
                        help="group_3 files")
    #NEED TO MAKE A CONFIG FILE!
    parser.add_argument('--config_file', '-c', action='store', type=str, dest='config',
                        required=True, help='config file (pickle)')
    #############
    parser.add_argument('-nb_files', '-nb', action='store', dest='nb_files', required=False,
                        default=50, type=int, help="maximum number of reads to use")
    parser.add_argument('--jobs', '-j', action='store', dest='jobs', required=False,
                        default=4, type=int, help="number of jobs to run concurrently")
    parser.add_argument('--iter', '-i', action='store', dest='iter', required=False,
                        default=1, type=int, help="number of iterations to do")
    parser.add_argument('--learning_algorithm', '-a', dest='learning_algo', required=False,
                        default=None, action='store', type=str, help="options: \"annealing\"")
    parser.add_argument('--epochs', '-ep', action='store', dest='epochs', required=False,
                        default=10000, type=int, help="number of iterations to do")
    parser.add_argument('--batch_size', '-b', action='store', dest='batch_size', required=False, type=int,
                        default=None, help='specify batch size')
    parser.add_argument('--learning_rate', '-e', action='store', dest='learning_rate',
                        required=False, default=0.01, type=float)
    parser.add_argument('--L1_reg', '-L1', action='store', dest='L1', required=False,
                        default=0.0, type=float)
    parser.add_argument('--L2_reg', '-L2', action='store', dest='L2', required=False,
                        default=0.001, type=float)
    parser.add_argument('--train_test', '-s', action='store', dest='split', required=False,
                        default=0.9, type=float, help="train/test split")
    parser.add_argument('--preprocess', '-p', action='store', required=False, default=None,
                        dest='preprocess', help="options:\nnormalize\ncenter\ndefault:None")
    parser.add_argument('--output_location', '-o', action='store', dest='out',
                        required=True, type=str, default=None,
                        help="directory to put results")
    args = parser.parse_args()
    return args
