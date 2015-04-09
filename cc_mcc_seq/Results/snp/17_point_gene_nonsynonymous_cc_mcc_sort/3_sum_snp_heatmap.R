data=read.table('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_2group_cc_sorted_c',sep='\t',header=F,row.names=1)
data=data[,4:ncol(data)]
colnames(data)=c('10A','1A','2A','3A','4A','5A','6A','7A','8A','9A','10MA','1MA','2MA','3MA','4MA','5MA','6MA','7MA','8MA','9MA')
data=as.matrix(data)
ColSideColors=rep(c('#DD56DB','#E5CC37'), each =10)
#hv=heatmap(data,scale="none",col=topo.colors(100),keep.dendro=T,Colv=NA,ColSideColors=SideColors)
library(gplots)
pdf('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_2group_cc_sorted_c.pdf')
hv=heatmap.2(data,col=topo.colors(75),scale="none",ColSideColors=ColSideColors,key=TRUE, symkey=FALSE, density.info="none",trace="none",Colv=NA,margins=c(5,10))
dev.off()


data=read.table('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_2group_mcc_sorted_c',sep='\t',header=F,row.names=1)
data=data[,4:ncol(data)]
colnames(data)=c('10A','1A','2A','3A','4A','5A','6A','7A','8A','9A','10MA','1MA','2MA','3MA','4MA','5MA','6MA','7MA','8MA','9MA')
data=as.matrix(data)
ColSideColors=rep(c('#DD56DB','#E5CC37'), each =10)
#hv=heatmap(data,scale="none",col=topo.colors(100),keep.dendro=T,Colv=NA,ColSideColors=SideColors)
library(gplots)
pdf('sum_snp.exome_combined.sorted.pass012.new.gene_ttest_2group_mcc_sorted_c.pdf')
hv=heatmap.2(data,col=topo.colors(75),scale="none",ColSideColors=ColSideColors,key=TRUE, symkey=FALSE, density.info="none",trace="none",Colv=NA,margins=c(5,10))
dev.off()
