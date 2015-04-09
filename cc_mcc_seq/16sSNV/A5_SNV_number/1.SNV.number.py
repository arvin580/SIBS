file1=['SNV.genome.ICC4A','SNV.genome.ICC4B','SNV.genome.somatic.ICC4']
file2=['SNV.genome.ICC5A','SNV.genome.ICC5B','SNV.genome.somatic.ICC5']
file3=['SNV.genome.ICC9A','SNV.genome.ICC9B','SNV.genome.somatic.ICC9']
file4=['SNV.genome.ICC10A','SNV.genome.ICC10B','SNV.genome.somatic.ICC10']
file5=['SNV.genome.CHC5A','SNV.genome.CHC5B','SNV.genome.somatic.CHC5']
file6=['SNV.genome.CHC6A','SNV.genome.CHC6B','SNV.genome.somatic.CHC6']
file7=['SNV.genome.CHC7A','SNV.genome.CHC7B','SNV.genome.somatic.CHC7']
file8=['SNV.genome.CHC10A','SNV.genome.CHC10B','SNV.genome.somatic.CHC10']

file=[file1,file2,file3,file4,file5,file6,file7,file8]
ouFile=open('genome_SNV_number','w')

for i in file :
    ouFile.write(i[2].split('.')[-1]+'\t')
    for j in i :
        print(j)
        inFile=open(j)
        d=inFile.readlines()
        ouFile.write(str(len(d))+'\t')
        inFile.close()
    ouFile.write('\n')
ouFile.close()




file1=['SNV.exome.ICC4A','SNV.exome.ICC4B','SNV.exome.somatic.ICC4']
file2=['SNV.exome.ICC5A','SNV.exome.ICC5B','SNV.exome.somatic.ICC5']
file3=['SNV.exome.ICC9A','SNV.exome.ICC9B','SNV.exome.somatic.ICC9']
file4=['SNV.exome.ICC10A','SNV.exome.ICC10B','SNV.exome.somatic.ICC10']
file5=['SNV.exome.CHC5A','SNV.exome.CHC5B','SNV.exome.somatic.CHC5']
file6=['SNV.exome.CHC6A','SNV.exome.CHC6B','SNV.exome.somatic.CHC6']
file7=['SNV.exome.CHC7A','SNV.exome.CHC7B','SNV.exome.somatic.CHC7']
file8=['SNV.exome.CHC10A','SNV.exome.CHC10B','SNV.exome.somatic.CHC10']

file=[file1,file2,file3,file4,file5,file6,file7,file8]
ouFile=open('exome_SNV_number','w')

for i in file :
    ouFile.write(i[2].split('.')[-1]+'\t')
    for j in i :
        print(j)
        inFile=open(j)
        d=inFile.readlines()
        ouFile.write(str(len(d))+'\t')
        inFile.close()
    ouFile.write('\n')
ouFile.close()
