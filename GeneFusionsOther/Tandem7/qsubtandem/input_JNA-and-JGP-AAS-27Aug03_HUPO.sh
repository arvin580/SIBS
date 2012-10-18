#!/bin/bash
### Job name
#LJRS -N tandem
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

cd /netshare1/home1/people/hansun/GeneFusionsOther/Tandem7

tandem.exe inputxml/input_JNA-and-JGP-AAS-27Aug03_HUPO.xml
