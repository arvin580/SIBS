cd /netshare1/home1/szzhongxin/proj1/hansun/12sSV/delly 
qsub delly.ICC1A.sh -l nodes=n4
qsub delly.ICC2A.sh -l nodes=n5
qsub delly.ICC3A.sh -l nodes=n6
qsub delly.ICC6A.sh -l nodes=n7
qsub delly.ICC7A.sh -l nodes=n9
qsub delly.ICC8A.sh -l nodes=n10

qsub delly.CHC1A.sh -l nodes=n11
qsub delly.CHC2A.sh -l nodes=n12
qsub delly.CHC3A.sh -l nodes=n13
qsub delly.CHC4A.sh -l nodes=n14
qsub delly.CHC8A.sh -l nodes=n15
qsub delly.CHC9A.sh -l nodes=n16
