inFile=open('sum_snp.genome_combined.sorted.pass012.new_cc')
total=0


for line in inFile :
    line=line.strip()
    fields=line.split()
    for item in fields[-20:-10] :
        total+=int(item)

inFile.close()

print(total)


length=0
inFile=open('/netshare1/home1/people/hansun/Data/hg19_refGene/hg19.chr.len')
for line in inFile :
    line=line.strip()
    fields=line.split()
    length+=int(fields[1])


inFile.close()

print(length)
