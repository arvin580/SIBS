inFile=open('sum_snp.genome_combined.sorted.pass012')

transition=0
tranversion=0

for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    if (fields[24]=='A' and fields[25]=='T') or (fields[24]=='T' and fields[25]=='A') \
            or (fields[24]=='C' and fields[25]=='G') or (fields[24]=='G' and fields[25]=='C') :

        transition+=1
    else :
        tranversion+=1

inFile.close()

print(transition)
print(tranversion)
