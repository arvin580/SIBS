inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-more_than_one')
ouFile1 = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-virus-site','w')
ouFile2 = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-virus-site-region-unique','w')
ouFile3 = open('ERR0498-04-05.unmapped.unique.human-viruse-checked-virus-site-region-unique2','w')
chs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16',
        'chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']
VIRUS = 'NC_001357.1'
D = {}
I = 100
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

        if ch1 == VIRUS:
            if (pos1_query+pos2_query) < (pos3_query+pos4_query): 
                ouFile1.write(VIRUS+'\t'+str(pos2_subject)+'\n')
                D.setdefault(VIRUS+'\t'+str(pos2_subject),[])
                flag = 0
                for item in D[VIRUS+'\t'+str(pos2_subject)]:
                    if pos3_subject -I <= item[0] <= pos3_subject + I or \
                        pos4_subject -I <= item[0] <= pos4_subject + I or \
                        pos3_subject -I <= item[1] <= pos3_subject + I or \
                        pos4_subject -I <= item[1] <= pos4_subject + I :
                            flag += 1
                if flag == 0:
                    D[VIRUS+'\t'+str(pos2_subject)].append([pos3_subject,pos4_subject])
            else:
                ouFile1.write(VIRUS+'\t'+str(pos1_subject)+'\n')
                D.setdefault(VIRUS+'\t'+str(pos1_subject),[])
                flag = 0
                for item in D[VIRUS+'\t'+str(pos1_subject)]:
                    if pos3_subject -I <= item[0] <= pos3_subject + I or \
                        pos4_subject -I <= item[0] <= pos4_subject + I or \
                        pos3_subject -I <= item[1] <= pos3_subject + I or \
                        pos4_subject -I <= item[1] <= pos4_subject + I :
                            flag += 1
                if flag == 0:
                    D[VIRUS+'\t'+str(pos1_subject)].append([pos3_subject,pos4_subject])

        elif ch2 == VIRUS:
            if (pos3_query+pos4_query) < (pos1_query+pos2_query): 
                ouFile1.write(VIRUS+'\t'+str(pos4_subject)+'\n')
                D.setdefault(VIRUS+'\t'+str(pos4_subject),[])
                flag = 0
                for item in D[VIRUS+'\t'+str(pos4_subject)]:
                    if pos1_subject -I <= item[0] <= pos1_subject + I or \
                        pos2_subject -I <= item[0] <= pos2_subject + I or \
                        pos1_subject -I <= item[1] <= pos1_subject + I or \
                        pos2_subject -I <= item[1] <= pos2_subject + I :
                            flag += 1
                if flag == 0:
                    D[VIRUS+'\t'+str(pos4_subject)].append([pos1_subject,pos2_subject])


            else:
                ouFile1.write(VIRUS+'\t'+str(pos3_subject)+'\n')
                D.setdefault(VIRUS+'\t'+str(pos3_subject),[])
                flag = 0
                for item in D[VIRUS+'\t'+str(pos3_subject)]:
                    if pos1_subject -I <= item[0] <= pos1_subject + I or \
                        pos2_subject -I <= item[0] <= pos2_subject + I or \
                        pos1_subject -I <= item[1] <= pos1_subject + I or \
                        pos2_subject -I <= item[1] <= pos2_subject + I :
                            flag += 1
                if flag == 0:
                    D[VIRUS+'\t'+str(pos3_subject)].append([pos1_subject,pos2_subject])

    else:
        break

d = D.items()
d.sort(cmp=lambda x,y:cmp(len(x[1]),len(y[1])),reverse=True)
for item in d:
    ouFile2.write(item[0]+'\n')
    ouFile3.write(item[0]+'\t'+str(len(item[1]))+'\n')


inFile.close()
ouFile1.close()
ouFile2.close()
ouFile3.close()
