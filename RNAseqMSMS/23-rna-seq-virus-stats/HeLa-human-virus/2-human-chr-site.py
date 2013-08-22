def human_chr_site(inF):
    inFile = open(inF)
    ouFile1 = open(inF+'-human-chr-site','w')
    ouFile2 = open(inF+'-human-chr-site-unique','w')
    ouFile3 = open(inF+'-human-chr-site-unique2','w')
    chs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
            'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']
    D = {}
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            ch1 = fields[3]
            ch2 = fields[15]
            pos1_query = int(fields[8])
            pos2_query = int(fields[9])
            pos3_query = int(fields[20])
            pos4_query = int(fields[21])
            pos1_subject = int(fields[10])
            pos2_subject = int(fields[11])
            pos3_subject = int(fields[22])
            pos4_subject = int(fields[23])
    
            if ch1 in chs:
                if (pos1_query+pos2_query) < (pos3_query+pos4_query): 
                    ouFile1.write(ch1+'\t'+str(pos2_subject)+'\n')
                    D.setdefault(ch1+'\t'+str(pos2_subject),0)
                    D[ch1+'\t'+str(pos2_subject)]+=1
                else:
                    ouFile1.write(ch1+'\t'+str(pos1_subject)+'\n')
                    D.setdefault(ch1+'\t'+str(pos1_subject),0)
                    D[ch1+'\t'+str(pos1_subject)]+=1
            elif ch2 in chs:
                if (pos3_query+pos4_query) < (pos1_query+pos2_query): 
                    ouFile1.write(ch2+'\t'+str(pos4_subject)+'\n')
                    D.setdefault(ch2+'\t'+str(pos4_subject),0)
                    D[ch2+'\t'+str(pos4_subject)]+=1
                else:
                    ouFile1.write(ch2+'\t'+str(pos3_subject)+'\n')
                    D.setdefault(ch2+'\t'+str(pos3_subject),0)
                    D[ch2+'\t'+str(pos3_subject)]+=1
    
        else:
            break
    
    d = D.items()
    d.sort(cmp=lambda x,y:cmp(x[1],y[1]),reverse=True)
    for item in d:
        ouFile2.write(item[0]+'\n')
        ouFile3.write(item[0]+'\t'+str(item[1])+'\n')
    
    
    inFile.close()
    ouFile1.close()
    ouFile2.close()
    ouFile3.close()

#human_chr_site('ERR0498-04-05.unmapped.unique.human-viruse-checked')
human_chr_site('ERR0498-04-05.unmapped.unique.human-viruse-checked-chr8-128230000-128250000')
