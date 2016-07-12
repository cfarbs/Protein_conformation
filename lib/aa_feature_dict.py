#!/usr/bin/env python

#Script to add features to amino acids to increase accuracy of network

def feature_dict():
    featurefilename = "aa_data_chart.txt"
    aminofile = open(featurefilename, 'r')
    Feature = {}
    LineNumber = 0
    Codes = []

    for Line in aminofile:
        if(LineNumber>0):
            Codes = Line.split(",")
            numb = int(Codes[0].strip("\n"))
            helicode = Codes[3].strip("\n")
            sheetcode = Codes[4].strip("\n")
            heliprop = Codes[5].strip("\n")
            sheetprop = Codes[6].strip("\n")
            aaweight = Codes[7].strip(" ")
            pkacarb = Codes[8].strip("\n")
            pkaamine = Codes[9].strip("\n")
            pkaR = Codes[10].strip("\n")
            numcarbs = Codes[11].strip("\n")
            numhyd = Codes[12].strip("\n")
            numnitro = Codes[13].strip("\n")
            numoxy = Codes[14].strip("\n")
            numsulfur = Codes[15].strip("\n")
            area = Codes[16].strip("\n")
            accessarea = Codes[17].strip("\n")
            buriedarea = Codes[18].strip("\n")
            arealoss = Codes[19].strip("\n")
            residmass = Codes[20].strip("\n")
            monoisomass = Codes[21].strip("\n")
            Feature[numb]=(float(aaweight))
        LineNumber = LineNumber + 1
    aminofile.close()
    return Feature
