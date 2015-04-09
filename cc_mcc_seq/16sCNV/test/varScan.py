import sys

R=r'''

library(DNAcopy)
cn <- read.table("%s",header=T)
CNA.object <-CNA( genomdat = cn[,7], chrom = cn[,1], maploc = cn[,2], data.type = 'logratio')
CNA.smoothed <- smooth.CNA(CNA.object)
segs <- segment(CNA.smoothed, verbose=0, min.width=2)
segs2 = segs$output
write.table(segs2[,2:6], file="%s.DNAcopyed", row.names=F, col.names=F, quote=F, sep="\t")
pdf("%s.pdf")
plot(segs, plot.type="w")
dev.off()

'''%(sys.argv[1],sys.argv[1],sys.argv[1])

from Rscript.RscriptClass import *
Rscript(R)

