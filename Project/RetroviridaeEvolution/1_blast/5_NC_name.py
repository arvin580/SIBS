inFile=open('/netshare1/home1/people/hansun/Data/RetroviridaeGenome/RetroviridaeGenome.fasta.fa')
ouFile=open('RetroviridaeGenome.fasta.fa.head','w')
for line in inFile :
    if line.find('>') ==0 :
        ouFile.write(line)
inFile.close()


inFile=open('RetroviridaeGenome.fasta.fa.head_c')
dict1=dict()
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    dict1[fields[0]]=fields[1]
inFile.close()

inFile=open('blast_result2')
ouFile=open('blast_result3','w')

head=inFile.readline()
ouFile.write('name'+'\t'+head)
for line in inFile :
    line=line.strip()
    fields=line.split('\t')
    ouFile.write(dict1[fields[0]]+'\t'+line+'\n')

inFile.close()
ouFile.close()
