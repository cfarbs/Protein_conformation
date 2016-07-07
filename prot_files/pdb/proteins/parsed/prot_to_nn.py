#!/usr/bin/env python

#script to convert parsed data into useable format

#imports amino acid to number dictionary
from prot_to_num import amino_dict
#required for order dictionary creation
import collections

#method to create a reversed list that also enumerates in reverse.
#http://galvanist.com/post/53478841501/python-reverse-enumerate -
#updated for python3
def reverse_enumerate(iterable):
    """
    Enumerate over an iterable in reverse order while retaining proper indexes
    """
    return zip(reversed(range(len(iterable))), reversed(iterable))

#find that AA, by Art
def find_it(start, search_length, b_target, e_target, target_len, arr):
    for _ in range(start, (start - search_length), -1):
        if arr[_] == b_target:
            if arr[_ + (target_len - 1)] == e_target:
                return " ".join(arr[_:_ + target_len])
            else:
                pass
        else:
            continue


#local variable to store amino acid dictionary
aa_dict = amino_dict()

#select pdb file to open using pdb id as input.
#Currently only allows one file at a time.
pdbID = input("PDB ID of protein to parse?")
infilename = pdbID + ".pdb.gz.txt"
#if id ends w/P, returns without p. i.e. 1a0p.pdb.gz.txt -> 1a0 (?)
infile = open(infilename,'r')
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
        else:
            if len(data[0]) <= 3:
                #parse helix info
                helixnum = data[0]
                initamino = data[1]
                initseq = data[2]
                finamino = data[3]
                finseq = data[4]
                lenhelix = data[5]
                heli = [int(initseq), int(finseq), int(lenhelix), initamino, finamino]
                helinfo[helixnum] = heli
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
        pass





#list to store amino acids converted to numbers
digitseq = []
#change amino acids to numbers in a list.
for aa in range(len(protseq)):
    digitseq.append(int(str(aa_dict[protseq[aa]])))


digithelix = []
for count, aa in enumerate(helist):
    aastring = aa.split(" ")
    for residue in range(len(aastring)):
        tempdigi = int(str(aa_dict[aastring[residue]]))
        print (tempdigi)
        #digithelix.append(temple)

#print (pdbID)
#print (helinfo)
#print (digitseq)
#print (digithelix)


"""if protseq(acids) == helinfo[helix][3]:
    helistring = protseq[acids:acids+helinfo[helix][2]]
    print (helistring)"""



#PLAN: PRINT TO SEPARATE FILE; SEPARATE FILES OR ALL TOGETHER?
infile.close()
