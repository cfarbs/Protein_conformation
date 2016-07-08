#!/usr/bin/env python

#script to convert parsed data into useable format

#imports amino acid to number dictionary
from prot_to_num import amino_dict
#required for order dictionary creation
import collections
import glob
import os
#find that AA, by Art
def find_it(start, search_length, b_target, e_target, target_len, arr):
    for _ in range(start, (start - search_length), -1):
        try:
            if arr[_] == b_target:
                if arr[_ + (target_len - 1)] == e_target:
                    return " ".join(arr[_:_ + target_len])
                else:
                    pass
            else:
                continue
        except:
            pass

Outfilename = "ParseErrors.txt"
OutFile = open(Outfilename, 'w')
#local variable to store amino acid dictionary
aa_dict = amino_dict()

filelist = sorted(glob.glob('./*.pdb.gz.txt'))

#filecount = 0
for name in filelist:
    infile = open(name, 'r')
    errorlist=[]
    seqerrors = 0
    helixerrors = 0
    helisterrors = 0
    helix2numerrors= 0
    pdbID = name[2:6]
    #select pdb file to open using pdb id as input.
    #Currently only allows one file at a time.
    #list to contain protein sequence
    protseq = []
    #ordered dictionary to store helix information
    helinfo = collections.OrderedDict()
    #to skip header line of pdb files
    LineNumber = 0
    #initializes lenhelix as an integer
    lenhelix = 0
    helist = []
    #for loop to parse out protein sequence and helix data
    for line in infile:
        if(LineNumber>0):
            lines = line.strip("\n")
            data = lines.split(" ")
            first = line[0]
            #Parse out protein sequence
            if first.isdigit() == False:
                if len(data[0]) == 3:
                    if first == "H":
                        if data[0] == "HIS":
                            #remove blank indices from sequence
                            fildata = list(filter(None, data))
                            protseq += fildata
                        else:
                            pass
                    else:
                        fildata = list(filter(None, data))
                        protseq += fildata
                if len(data[0]) == 1 or 2:
                    seqerrors +=1
            else:
                if len(data[0]) <= 3:
                    #parse helix info
                    helixnum = data[0]
                    initamino = data[1]
                    initseq = data[2]
                    finamino = data[3]
                    finseq = data[4]
                    lenhelix = data[5]
                    try:
                        heli = [int(initseq), int(finseq), int(lenhelix), initamino, finamino]
                        helinfo[helixnum] = heli
                    except:
                        #print ("Error in parsing helix data for %s" % (pdbID))
                        helixerrors +=1
                else:
                    pass
        LineNumber += 1

    #for loop to loop through protein sequence and isolate windows where
    for helix in helinfo.keys():
        helength = helinfo[helix][2]
        if helength >= 12:
            initpos = helinfo[helix][0]
            finalpos = helinfo[helix][1]
            initaa = helinfo[helix][3]
            finaa = helinfo[helix][4]
            helices = find_it(start=initpos,search_length=helength,b_target=initaa,e_target=finaa,target_len=helength,arr=protseq)
            helist.append(helices)
        else:
            helisterrors += 1





    #list to store amino acids converted to numbers
    digitseq = []
    #change amino acids to numbers in a list.
    for aa in range(len(protseq)):
        digitseq.append(int(str(aa_dict[protseq[aa]])))


    digithelix = []

    for count, aa in enumerate(helist):
        try:
            tempdigi = []
            aastring = aa.split(" ")
            aashort = aastring[:12]
            for residue in range(len(aashort)):
                tempdigi.append(aa_dict[aashort[residue]])
                if len(tempdigi) == len(aashort):
                    digithelix.append(tempdigi)
        except:
            #print ("Something is wrong with %s's helices" % (pdbID))
            helix2numerrors += 1

    infile.close()

    outstring = "%s Sequence Parse Errors: %d; Helix Parse Errors: %d; Helix Extraction Errors: %d; Helix to Digit Errors: %d" % (pdbID, seqerrors, helixerrors, helisterrors, helix2numerrors)
    OutFile.write(outstring + "\n")
    #try:

        #print (pdbID)
        #print (helinfo)
        #print (digitseq)
        #print (digithelix)
    #except:
        #pass
#print (filecount)

OutFile.close()
#PLAN: PRINT TO SEPARATE FILE; SEPARATE FILES OR ALL TOGETHER?
