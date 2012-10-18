#!/bin/bash
### Job name
#LJRS -N tandem 
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

# This job's working directory
cd /netshare1/home1/people/hansun/S_GeneFusions/Tandem
tandem.exe inputxml/input_ADC_A_nw_050707n_lung_AD_A08.xml
