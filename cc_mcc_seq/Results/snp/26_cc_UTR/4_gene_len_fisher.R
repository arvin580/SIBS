data=read.table('sum_snp.exome_combined.sorted.pass012.new_cc_num_len')
write.table(NA,'sum_snp.exome_combined.sorted.pass012.new_cc_num_len_fisher',append=F,sep='\t',row.names=F,col.names=F,quote=F)

for(i in 1:nrow(data)) 
{

fs=fisher.test(c(data[i,2],data[i,3]),c(329633,3000000000))
row_data=cbind(data[i,1:3],fs$p)

write.table(row_data,'sum_snp.exome_combined.sorted.pass012.new_cc_num_len_fisher',append=T,sep='\t',row.names=F,col.names=F,quote=F)


}
