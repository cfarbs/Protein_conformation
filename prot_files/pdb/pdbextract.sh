#!/bin/bash

for file in *.gz
do
gunzip -c $file > proteins/$file
done
