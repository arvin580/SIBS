file1=['SNV.genome.ICC4A.not.repeat','SNV.genome.ICC4B.not.repeat','SNV.genome.somatic.ICC4.not.repeat']
file2=['SNV.genome.ICC5A.not.repeat','SNV.genome.ICC5B.not.repeat','SNV.genome.somatic.ICC5.not.repeat']
file3=['SNV.genome.ICC9A.not.repeat','SNV.genome.ICC9B.not.repeat','SNV.genome.somatic.ICC9.not.repeat']
file4=['SNV.genome.ICC10A.not.repeat','SNV.genome.ICC10B.not.repeat','SNV.genome.somatic.ICC10.not.repeat']
file5=['SNV.genome.CHC5A.not.repeat','SNV.genome.CHC5B.not.repeat','SNV.genome.somatic.CHC5.not.repeat']
file6=['SNV.genome.CHC6A.not.repeat','SNV.genome.CHC6B.not.repeat','SNV.genome.somatic.CHC6.not.repeat']
file7=['SNV.genome.CHC7A.not.repeat','SNV.genome.CHC7B.not.repeat','SNV.genome.somatic.CHC7.not.repeat']
file8=['SNV.genome.CHC10A.not.repeat','SNV.genome.CHC10B.not.repeat','SNV.genome.somatic.CHC10.not.repeat']

file=[file1,file2,file3,file4,file5,file6,file7,file8]
ouFile=open('genome_SNV_number','w')

for i in file :
    ouFile.write(i[2].split('.')[-4]+'\t')
    for j in i :
        print(j)
        inFile=open(j)
        d=inFile.readlines()
        ouFile.write(str(len(d))+'\t')
        inFile.close()
    ouFile.write('\n')
ouFile.close()




file1=['SNV.exome.ICC4A.not.repeat','SNV.exome.ICC4B.not.repeat','SNV.exome.somatic.ICC4.not.repeat.mc']
file2=['SNV.exome.ICC5A.not.repeat','SNV.exome.ICC5B.not.repeat','SNV.exome.somatic.ICC5.not.repeat.mc']
file3=['SNV.exome.ICC9A.not.repeat','SNV.exome.ICC9B.not.repeat','SNV.exome.somatic.ICC9.not.repeat.mc']
file4=['SNV.exome.ICC10A.not.repeat','SNV.exome.ICC10B.not.repeat','SNV.exome.somatic.ICC10.not.repeat.mc']
file5=['SNV.exome.CHC5A.not.repeat','SNV.exome.CHC5B.not.repeat','SNV.exome.somatic.CHC5.not.repeat.mc']
file6=['SNV.exome.CHC6A.not.repeat','SNV.exome.CHC6B.not.repeat','SNV.exome.somatic.CHC6.not.repeat.mc']
file7=['SNV.exome.CHC7A.not.repeat','SNV.exome.CHC7B.not.repeat','SNV.exome.somatic.CHC7.not.repeat.mc']
file8=['SNV.exome.CHC10A.not.repeat','SNV.exome.CHC10B.not.repeat','SNV.exome.somatic.CHC10.not.repeat.mc']

file=[file1,file2,file3,file4,file5,file6,file7,file8]
ouFile=open('exome_SNV_number','w')

for i in file :
    ouFile.write(i[2].split('.')[-4]+'\t')
    for j in i :
        print(j)
        inFile=open(j)
        d=inFile.readlines()
        ouFile.write(str(len(d))+'\t')
        inFile.close()
    ouFile.write('\n')
ouFile.close()
