data=read.table('sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted_cc_num_len2_fisher')
data=as.matrix(data)
name=data[,1]
fisher=data[,2]
fdr=p.adjust(fisher,'fdr',length(fisher))
out=cbind(name,fdr)
write.table(out,'sum_snp.genome_combined.sorted.pass012.new.UTR.genesorted_cc_num_len2_fisher.fdr',quote=F,sep='\t',row.names=F,col.names=F)

