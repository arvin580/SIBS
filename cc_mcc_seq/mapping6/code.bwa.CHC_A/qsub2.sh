cd /netshare1/home1/szzhongxin/proj1/hansun/Viruses/code.bwa.CHC_A

#qsub bwa10a.pbs -l nodes=n12 -q high
#qsub bwa1a.pbs -l nodes=n11:ppn=6
#qsub bwa2a.pbs -l nodes=n11:ppn=6
#qsub bwa3a.pbs -l nodes=n11:ppn=6
#qsub bwa4a.pbs -l nodes=n5:ppn=6 -q high
qsub bwa5a.pbs -l nodes=n4 -q high
qsub bwa6a.pbs -l nodes=n5 -q high
##qsub bwa7a.pbs -l nodes=n15 -q high
#qsub bwa8a.pbs -l nodes=n11:ppn=6
#qsub bwa9a.pbs -l nodes=n11:ppn=6 -q high
