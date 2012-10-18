#!/bin/bash
### Job name
#LJRS -N parser 
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

# This job's working directory
cd /netshare1/home1/people/hansun/GeneFusions/AftTandem
perl tandem_xml_parser.pl output FDR FDR_fusions
