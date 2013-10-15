inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two.fa','w')

for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    
    info = fields[0] + ':' + fields[1]
    for i in range(10,len(fields),26):
        pos1 = fields[i]
        pos2 = fields[i+1]
        pos3 = fields[i+12]
        pos4 = fields[i+13]
        seq = fields[i+18].split('|')[0]
        seq_id = fields[i-6]
        ouFile.write('>'+info+'\t'+seq_id+'\t'+'\t'.join([pos1,pos2,pos3,pos4])+'\n')
        ouFile.write(seq+'\n')

inFile.close()
