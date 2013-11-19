#!/bin/bash
# Main script that oversees XAS analysis process. Takes in an xyz file, generates snapshots by creating noise, submits calculations to Shirley, and in parallel calculates coordinates like distance and angle between every single atom and an excited atom for every single excited atom in every snapshot.

# Parameters:
# $1 = xyz file
# $2 = temperature
# $3 = number of snapshots
# $4 = excited atoms with their line numbers
#xyzfile=$1; shift
#temperature=$1; shift
#numbersnaps=$1; shift

# Step 1: Generate noise
#python noisify.py $xyzfile $temperature $numbersnaps > noise.xyz

# Step 2: Send to Shirley
#later

# Step 3: Calculate coordinates and print them out
#python xyz_parser.py $xyzfile $@ > coordinate_data

# Step 4: Analyze results of Step 2 and 3

xyzfile=$1;
rm -rf histograms
mkdir histograms
cd histograms
python ../Init_Relationships.py ../$xyzfile
../gnuplot_stuff.sh *
cd ..
rm *.pyc
