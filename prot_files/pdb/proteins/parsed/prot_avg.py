#!/usr/bin/env python
import sys

for i in range(len(sys.argv)):
    if sys.argv[i] == "-protseq":
        infilename = sys.argv[i+1]
    else:
        pass


#print (infilename)
infile = open(infilename,'r')

value = 0
LineNumber = 0
numhelix = 0
for line in infile:
    if(LineNumber>0):
        lines = line.strip("\n")
        data = lines.split(" ")
        first = line[0]
        #Parse out protein sequence
        if first.isdigit() == False:
            pass
        elif len(data[1]) == 3:
            numhelix +=1
            #parse helix info
            #print (data)
            helixnum = data[0]
            initamino = data[1]
            initseq = data[2]
            finamino = data[3]
            finseq = data[4]
            lenhelix = int(data[5])
            value += lenhelix
    LineNumber += 1

infile.close()

try:
    print (value/numhelix)
except ZeroDivisionError:
    pass
