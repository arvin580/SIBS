library(DNAcopy)
cn <- read.table("varScan.ICC5.chr1.copynumber.called",header=T)
CNA.object <-CNA( genomdat = cn[,7], chrom = cn[,1], maploc = cn[,2], data.type = 'logratio', sampleid = "ICC5.chr1"
)
CNA.smoothed <- smooth.CNA(CNA.object)
segs <- segment(CNA.smoothed, verbose=0, min.width=2)
segs2 = segs$output
write.table(segs2[,2:6], file="varScan.ICC5.chr1.copynumber.called.DNAcopyed", row.names=F, col.names=F, quote=F, sep="\t")
pdf("varScan.ICC5.chr1.copynumber.called.pdf")
plot(segs, plot.type="w")
dev.off()