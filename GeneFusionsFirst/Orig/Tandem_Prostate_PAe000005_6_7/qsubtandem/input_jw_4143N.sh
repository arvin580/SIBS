#!/bin/bash
### Job name
#LJRS -N tandem
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

cd /netshare1/home1/people/hansun/GeneFusions/Tandem_Prostate_PAe000005_6_7

tandem.exe inputxml/input_jw_4143N.xml
