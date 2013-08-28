library(DNAcopy)
cn <- read.table("varScan.P1N1.chr10.copynumber.called",header=T)
CNA.object <-CNA( genomdat = cn[,7], chrom = cn[,1], maploc = cn[,2], data.type = 'logratio', sampleid = "P1N1.chr10"
)
CNA.smoothed <- smooth.CNA(CNA.object)
segs <- segment(CNA.smoothed, verbose=0, min.width=2)
segs2 = segs$output
write.table(segs2[,2:6], file="varScan.P1N1.chr10.copynumber.called.DNAcopyed", row.names=F, col.names=F, quote=F, sep="\t")
pdf("varScan.P1N1.chr10.copynumber.called.pdf")
plot(segs, plot.type="w")
dev.off()