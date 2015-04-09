cd /netshare1/home1/szzhongxin/proj1/hansun/12sSV/duppy 
qsub duppy.ICC1A.sh -l nodes=n4
qsub duppy.ICC2A.sh -l nodes=n5
qsub duppy.ICC3A.sh -l nodes=n6
qsub duppy.ICC6A.sh -l nodes=n7
qsub duppy.ICC7A.sh -l nodes=n9
qsub duppy.ICC8A.sh -l nodes=n10

qsub duppy.CHC1A.sh -l nodes=n11
qsub duppy.CHC2A.sh -l nodes=n12
qsub duppy.CHC3A.sh -l nodes=n13
qsub duppy.CHC4A.sh -l nodes=n14
qsub duppy.CHC8A.sh -l nodes=n15
qsub duppy.CHC9A.sh -l nodes=n16
