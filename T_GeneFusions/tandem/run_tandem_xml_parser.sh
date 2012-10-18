#!/bin/bash
### Job name
#LJRS -N tandem 
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

# This job's working directory
cd /netshare1/home1/people/hansun/GeneFusions/tandem
perl tandem_xml_parser.pl output output_aft_fdr output_aft_fdr_fusions
