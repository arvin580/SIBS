cd /netshare1/home1/szzhongxin/proj1/hansun/16sSV/jumpy/1_jumpy_results
#qsub 2.blastn.CHC10A.sh -l nodes=n11
#qsub 2.blastn.CHC10B.sh -l nodes=n11
#qsub 2.blastn.CHC5A.sh -l nodes=n11
#qsub 2.blastn.CHC5B.sh -l nodes=n11
#qsub 2.blastn.CHC6A.sh -l nodes=n11
qsub 2.blastn.CHC6B.sh -l nodes=n3
qsub 2.blastn.CHC7A.sh -l nodes=n4
qsub 2.blastn.CHC7B.sh -l nodes=n5
#qsub 2.blastn.ICC10A.sh -l nodes=n11
qsub 2.blastn.ICC10B.sh -l nodes=n6
qsub 2.blastn.ICC4A.sh -l nodes=n7
qsub 2.blastn.ICC4B.sh -l nodes=n8
qsub 2.blastn.ICC5A.sh -l nodes=n9
###qsub 2.blastn.ICC5B.sh -l nodes=n10
qsub 2.blastn.ICC9A.sh -l nodes=n12
qsub 2.blastn.ICC9B.sh -l nodes=n13
