#qsub CountCovariates10b.pbs -l nodes=cu11
#qsub CountCovariates4b.pbs  -l nodes=cu12
#qsub CountCovariates5b.pbs -l nodes=cu13
#qsub CountCovariates9b.pbs -l nodes=cu14


qsub TableRecalibration10b.pbs -l nodes=cu11
qsub TableRecalibration4b.pbs  -l nodes=cu12
qsub TableRecalibration5b.pbs -l nodes=cu13
qsub TableRecalibration9b.pbs -l nodes=cu14
