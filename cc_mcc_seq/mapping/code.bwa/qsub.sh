cd /netshare1/home1/szzhongxin/proj1/hansun/mapping/code.bwa 

qsub bwa4ax.pbs -l nodes=cu15
qsub bwa4ay.pbs -l nodes=cu14
qsub bwa4az.pbs -l nodes=cu13

qsub bwa5ax.pbs -l nodes=cu12
qsub bwa5ay.pbs -l nodes=cu11


qsub bwa9a.pbs -l nodes=cu10

qsub bwa10a.pbs -l nodes=cu09

