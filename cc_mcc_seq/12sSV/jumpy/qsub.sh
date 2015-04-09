cd /netshare1/home1/szzhongxin/proj1/hansun/12sSV/jumpy
qsub jumpy.ICC1A.sh -l nodes=n4
qsub jumpy.ICC2A.sh -l nodes=n5
qsub jumpy.ICC3A.sh -l nodes=n6
qsub jumpy.ICC6A.sh -l nodes=n7
qsub jumpy.ICC7A.sh -l nodes=n9
qsub jumpy.ICC8A.sh -l nodes=n10

qsub jumpy.CHC1A.sh -l nodes=n11
qsub jumpy.CHC2A.sh -l nodes=n12
qsub jumpy.CHC3A.sh -l nodes=n13
qsub jumpy.CHC4A.sh -l nodes=n14
qsub jumpy.CHC8A.sh -l nodes=n15
qsub jumpy.CHC9A.sh -l nodes=n16
