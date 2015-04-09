data=read.table('sum_snp.exome_combined.sorted.pass012.new_mcc_num_len2_fisher')
data=as.matrix(data)
name=data[,1]
fisher=data[,2]
fdr=p.adjust(fisher,'fdr',length(fisher))
out=cbind(name,fdr)
write.table(out,'sum_snp.exome_combined.sorted.pass012.new_mcc_num_len2_fisher.fdr',quote=F,sep='\t',row.names=F,col.names=F)

