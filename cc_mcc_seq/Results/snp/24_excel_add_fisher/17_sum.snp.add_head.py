head=['cc_fisher','cc_fisher_fdr','mcc_fisher','mcc_fisher_fdr','cancercensus','8p','KEGG_fudan','KEGG_Cancer','Stemcell_Metastasis_Inflammation','Gene_ranksumtest','SNV_ranksumtest','Gene_ttest','SNV_ttest','Func','Gene','ExonicFunc','AAChange','Conserved','SegDup','ESP5400_ALL','1000g2012feb_ALL','dbSNP135','AVSIFT'
,'LJB_PhyloP','LJB_PhyloP_Pred','LJB_SIFT','LJB_SIFT_Pred','LJB_PolyPhen2','LJB_PolyPhen2_Pred','LJB_LRT','LJB_LRT_Pred',
'LRT_MutationTaster','LRT_MutationTaster_Pred','LJB_GERP++','Chr','Start','End','Ref','Obs','Otherinfo']


inFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus.fisher')
ouFile=open('sum_snp.exome_combined.sorted.pass012.new.nonsyn.genesorted.tpvalue.fd3type.keggcancer.fdkegg.8p.cancercensus.fisher.head','w')

ouFile.write('\t'.join(head)+'\n')

for line in inFile :
    ouFile.write(line)
inFile.close()

ouFile.close()
