inFile = open('sum_snp1234.genome_summary_candidate.sorted')
ouFile = open('sum_snp1234.genome_summary_candidate.sorted.filtered.somatic','w')

for line in inFile:
    fields = line.split('\t')
    if (int(fields[-1])==0 and int(fields[-9]) >0) or \
            (int(fields[-2])==0 and int(fields[-12])>0) or \
            (int(fields[-3])==0 and int(fields[-13])>0) or \
            (int(fields[-4])==0 and int(fields[-14])>0) or \
            (int(fields[-5])==0 and int(fields[-19])>0) or \
            (int(fields[-6])==0 and int(fields[-20])>0) or \
            (int(fields[-7])==0 and int(fields[-24])>0) or \
            (int(fields[-8])==0 and int(fields[-25])>0) :
        if fields[0].find('intronic')==-1 and fields[0].find('downstream')==-1 and fields[0].find('upstream')==-1:
            ouFile.write(line)

inFile.close()
ouFile.close()
