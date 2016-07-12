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
            numb = int(Codes[0].strip(" "))
            helicode = Codes[3].strip(" ")
            sheetcode = Codes[4].strip(" ")
            heliprop = Codes[5].strip(" ")
            sheetprop = Codes[6].strip(" ")
            aaweight = Codes[7].strip(" ")
            pkacarb = Codes[8].strip(" ")
            pkaamine = Codes[9].strip(" ")
            pkaR = Codes[10].strip(" ")
            numcarbs = Codes[11].strip(" ")
            numhyd = Codes[12].strip(" ")
            numnitro = Codes[13].strip(" ")
            numoxy = Codes[14].strip(" ")
            numsulfur = Codes[15].strip(" ")
            area = Codes[16].strip(" ")
            accessarea = Codes[17].strip(" ")
            buriedarea = Codes[18].strip(" ")
            arealoss = Codes[19].strip(" ")
            residmass = Codes[20].strip(" ")
            monoisomass = Codes[21].strip("\n")
            Feature[numb]=(float(aaweight))
        LineNumber = LineNumber + 1
    aminofile.close()
    return Feature
