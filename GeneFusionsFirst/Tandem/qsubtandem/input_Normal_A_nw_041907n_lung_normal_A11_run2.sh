#!/bin/bash
### Job name
#LJRS -N tandem
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

cd /netshare1/home1/people/hansun/GeneFusions/Tandem

tandem.exe inputxml/input_Normal_A_nw_041907n_lung_normal_A11_run2.xml
