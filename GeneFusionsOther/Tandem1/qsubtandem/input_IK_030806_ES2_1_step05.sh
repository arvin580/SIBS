#!/bin/bash
### Job name
#LJRS -N tandem
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

cd /netshare1/home1/people/hansun/GeneFusionsOther/Tandem1

tandem.exe inputxml/input_IK_030806_ES2_1_step05.xml
