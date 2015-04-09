dict1=dict()
inFile=open('sum_snp34.genome_summary.pass012.CHC10B')
for line in inFile :
    fields=line.split('\t')
    k=fields[1]+fields[2]
    dict1[k]=0
inFile.close()
print(len(dict1))

inFile=open('sum_snp2.genome_summary.pass012.CHC10A')
for line in inFile :
    fields=line.split('\t')
    k=fields[1]+fields[2]
    if k not in dict1 :
        print(k)
inFile.close()


