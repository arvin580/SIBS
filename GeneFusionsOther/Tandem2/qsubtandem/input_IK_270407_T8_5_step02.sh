#!/bin/bash
### Job name
#LJRS -N tandem
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

cd /netshare1/home1/people/hansun/GeneFusionsOther/Tandem2

tandem.exe inputxml/input_IK_270407_T8_5_step02.xml
