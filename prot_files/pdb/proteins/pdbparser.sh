#!/bin/bash

#script to parse ID, sequence, and 2ndary structures given .pdb or .ent files

for protein in *.pdb.gz
do
awk '/HEADER/' $protein | awk '{print $1,$2,$3,$5}' > $protein.txt
awk '/HELIX/' $protein | awk '{print  $3, $4, $6, $7, $9, $11}' >> $protein.txt
awk '/SEQRES/' $protein | awk '{print $5, $6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17}' >> $protein.txt
done
