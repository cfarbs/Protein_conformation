#!/usr/bin/env python

infilenam = input("PDB ID of protein to parse?")
infilename = infilenam + ".pdb.gz.txt"
#if id ends w/P, returns without p. i.e. 1a0p.pdb.gz.txt -> 1a0 (?)
pdbID = infilename.strip(".pdb.gz.txt")
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

print (value/numhelix)
