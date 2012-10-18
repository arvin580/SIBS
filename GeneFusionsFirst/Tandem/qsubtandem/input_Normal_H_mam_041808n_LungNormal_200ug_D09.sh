#!/bin/bash
### Job name
#LJRS -N tandem
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

cd /netshare1/home1/people/hansun/GeneFusions/Tandem

tandem.exe inputxml/input_Normal_H_mam_041808n_LungNormal_200ug_D09.xml
