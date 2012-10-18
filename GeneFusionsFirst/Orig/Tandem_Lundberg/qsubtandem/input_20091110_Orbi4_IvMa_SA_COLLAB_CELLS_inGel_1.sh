#!/bin/bash
### Job name
#LJRS -N tandem
### Queue name
#LJRS -q dpool
### Number of nodes
#LJRS -l nodes=2:ppn=4

cd /netshare1/home1/people/hansun/GeneFusions/Tandem_Lundberg

tandem.exe inputxml/input_20091110_Orbi4_IvMa_SA_COLLAB_CELLS_inGel_1.xml
