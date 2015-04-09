cd /netshare1/home1/szzhongxin/proj1/hansun/12sSV/invy 
qsub invy.ICC1A.sh -l nodes=n4
qsub invy.ICC2A.sh -l nodes=n5
qsub invy.ICC3A.sh -l nodes=n6
qsub invy.ICC6A.sh -l nodes=n7
qsub invy.ICC7A.sh -l nodes=n9
qsub invy.ICC8A.sh -l nodes=n10

qsub invy.CHC1A.sh -l nodes=n11
qsub invy.CHC2A.sh -l nodes=n12
qsub invy.CHC3A.sh -l nodes=n13
qsub invy.CHC4A.sh -l nodes=n14
qsub invy.CHC8A.sh -l nodes=n15
qsub invy.CHC9A.sh -l nodes=n16
