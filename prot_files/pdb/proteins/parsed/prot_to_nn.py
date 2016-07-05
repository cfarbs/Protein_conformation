#!/usr/bin/env python

#script to convert parsed data into useable format
from prot_to_num import amino_dict


aa_dict = amino_dict()
infilenam = input("PDB ID of protein to parse?")
infilename = infilenam + ".pdb.gz.txt"
pdbID = infilename.strip(".pdb.gz.txt")
infile = open(infilename,'r')
#list to contain protein sequence
protseq = []

LineNumber = 0

for line in infile:
    if(LineNumber>0):
        lines = line.strip("\n")
        data = lines.split(" ")
        first = line[0]
        #Parse out protein sequence
        if first.isdigit() == False:
            #if data[0] == "DC" or "DT" or "DG":
                #pass
            #elif data[0] == "DA":
                #if len(data[1]) == 3:
                    #print (data[1])
            if len(data[0]) == 3:
                if first == "H":
                    if data[0] == "HIS":
                        #print (data)
                        #remove blank indices from sequence
                        fildata = list(filter(None, data))
                        protseq += fildata
                        #print (protseq)
                    else:
                        pass
                else:
                    #print (data)
                    fildata = list(filter(None, data))
                    protseq += fildata
                    #print (protseq)
        else:
            #parse helix info
            #print (data)
            helixnum = data[0]
            initamino = data[1]
            initseq = data[2]
            finamino = data[3]
            finseq = data[4]
            lenhelix = data[5]
            helinfo = (aa_dict[initamino], int(initseq), aa_dict[finamino], int(finseq), int(lenhelix))
    LineNumber += 1


#print (protseq)
#initialize amino acid digit list
digitseq = []
#change amino acids to numbers in a list.
for aa in range(len(protseq)):
    digitseq.append(int(str(aa_dict[protseq[aa]])))

print (pdbID)
print (helinfo)
print (digitseq)
infile.close()