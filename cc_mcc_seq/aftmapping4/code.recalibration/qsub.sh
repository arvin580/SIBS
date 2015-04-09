#qsub CountCovariates10b.pbs -l nodes=cu15
#qsub CountCovariates5b.pbs  -l nodes=cu16
#qsub CountCovariates6b.pbs -l nodes=cu17
#qsub CountCovariates7b.pbs -l nodes=cu18


qsub TableRecalibration10b.pbs -l nodes=cu15
qsub TableRecalibration5b.pbs  -l nodes=cu16
qsub TableRecalibration6b.pbs -l nodes=cu17
qsub TableRecalibration7b.pbs -l nodes=cu18
