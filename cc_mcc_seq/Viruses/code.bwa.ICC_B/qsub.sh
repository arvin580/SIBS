cd /netshare1/home1/szzhongxin/proj1/hansun/Viruses/code.bwa.ICC_B

qsub bwa10b.pbs -l nodes=n16:ppn=6 -q high
qsub bwa4b.pbs -l nodes=n17:ppn=6 -q high
qsub bwa5b.pbs -l nodes=n19:ppn=6 -q high
qsub bwa9b.pbs -l nodes=n21:ppn=6 -q high
