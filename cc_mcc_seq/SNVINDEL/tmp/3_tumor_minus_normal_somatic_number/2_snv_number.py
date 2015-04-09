file1=['sum_snp.genome_summary.pass012.ICC4A','sum_snp34.genome_summary.pass012.ICC4B','sum_snp.genome_summary.pass012.ICC4']
file2=['sum_snp.genome_summary.pass012.ICC5A','sum_snp34.genome_summary.pass012.ICC5B','sum_snp.genome_summary.pass012.ICC5']
file3=['sum_snp.genome_summary.pass012.ICC9A','sum_snp34.genome_summary.pass012.ICC9B','sum_snp.genome_summary.pass012.ICC9']
file4=['sum_snp.genome_summary.pass012.ICC10A','sum_snp34.genome_summary.pass012.ICC10B','sum_snp.genome_summary.pass012.ICC10']
file5=['sum_snp2.genome_summary.pass012.CHC5A','sum_snp34.genome_summary.pass012.CHC5B','sum_snp.genome_summary.pass012.CHC5']
file6=['sum_snp2.genome_summary.pass012.CHC6A','sum_snp34.genome_summary.pass012.CHC6B','sum_snp.genome_summary.pass012.CHC6']
file7=['sum_snp2.genome_summary.pass012.CHC7A','sum_snp34.genome_summary.pass012.CHC7B','sum_snp.genome_summary.pass012.CHC7']
file8=['sum_snp2.genome_summary.pass012.CHC10A','sum_snp34.genome_summary.pass012.CHC10B','sum_snp.genome_summary.pass012.CHC10']

file=[file1,file2,file3,file4,file5,file6,file7,file8]
ouFile=open('snv_number','w')

for i in file :
    for j in i :
        print(j)
        inFile=open(j)
        d=inFile.readlines()
        ouFile.write(str(len(d))+'\t')
        inFile.close()
    ouFile.write('\n')
ouFile.close()
