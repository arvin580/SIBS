library(DNAcopy)
cn <- read.table("varScan.CHC7.chr12.copynumber.called",header=T)
CNA.object <-CNA( genomdat = cn[,7], chrom = cn[,1], maploc = cn[,2], data.type = 'logratio', sampleid = "CHC7.chr12"
)
CNA.smoothed <- smooth.CNA(CNA.object)
segs <- segment(CNA.smoothed, verbose=0, min.width=2)
segs2 = segs$output
write.table(segs2[,2:6], file="varScan.CHC7.chr12.copynumber.called.DNAcopyed", row.names=F, col.names=F, quote=F, sep="\t")
pdf("varScan.CHC7.chr12.copynumber.called.pdf")
plot(segs, plot.type="w")
dev.off()