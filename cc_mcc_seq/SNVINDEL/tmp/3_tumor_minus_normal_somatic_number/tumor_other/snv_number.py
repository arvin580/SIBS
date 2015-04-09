file=['sum_snp.genome_summary.pass012.ICC10A10B',
'sum_snp.genome_summary.pass012.ICC10A4B',
'sum_snp.genome_summary.pass012.ICC10A5B',
'sum_snp.genome_summary.pass012.ICC10A9B',
'sum_snp.genome_summary.pass012.ICC4A10B',
'sum_snp.genome_summary.pass012.ICC4A4B',
'sum_snp.genome_summary.pass012.ICC4A5B',
'sum_snp.genome_summary.pass012.ICC4A9B',
'sum_snp.genome_summary.pass012.ICC5A10B',
'sum_snp.genome_summary.pass012.ICC5A4B',
'sum_snp.genome_summary.pass012.ICC5A5B',
'sum_snp.genome_summary.pass012.ICC5A9B',
'sum_snp.genome_summary.pass012.ICC9A10B',
'sum_snp.genome_summary.pass012.ICC9A4B',
'sum_snp.genome_summary.pass012.ICC9A5B',
'sum_snp.genome_summary.pass012.ICC9A9B',
'sum_snp.genome_summary.pass012.CHC10A10B',
'sum_snp.genome_summary.pass012.CHC10A5B',
'sum_snp.genome_summary.pass012.CHC10A6B',
'sum_snp.genome_summary.pass012.CHC10A7B',
'sum_snp.genome_summary.pass012.CHC5A10B',
'sum_snp.genome_summary.pass012.CHC5A5B',
'sum_snp.genome_summary.pass012.CHC5A6B',
'sum_snp.genome_summary.pass012.CHC5A7B',
'sum_snp.genome_summary.pass012.CHC6A10B',
'sum_snp.genome_summary.pass012.CHC6A5B',
'sum_snp.genome_summary.pass012.CHC6A6B',
'sum_snp.genome_summary.pass012.CHC6A7B',
'sum_snp.genome_summary.pass012.CHC7A10B',
'sum_snp.genome_summary.pass012.CHC7A5B',
'sum_snp.genome_summary.pass012.CHC7A6B',
'sum_snp.genome_summary.pass012.CHC7A7B']

ouFile=open('SNV_number','w')
for j in file :
    inFile=open(j)
    d=inFile.readlines()
    ouFile.write(j+'\t'+str(len(d))+'\n')
    inFile.close()
ouFile.close()


