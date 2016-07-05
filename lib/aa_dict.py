#!/usr/bin/env python

InFileName = "amino_acid_letter_code.txt"
InFile = open(InFileName, 'r')
Amino = {}
LineNumber = 0
Codes = []

for Line in InFile:
    if(LineNumber>0):
        Codes = Line.split(",")
        code = Codes[2].strip("\n")
        Amino[Codes[1]]=code
    LineNumber = LineNumber + 1
InFile.close()
