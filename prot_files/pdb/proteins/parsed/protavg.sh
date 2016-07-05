#!/bin/bash

rm protein_averages.txt

for protein in *.pdb.gz.txt
  do
  python prot_avg.py -protseq $protein >> protein_averages.txt
  done

for line in protein_averages.txt
  do
  awk '{sum+=$0;counter+=1}END{print sum/counter}'
  done
