inFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two.fa')
ouFile = open('ERR0498-04-05.unmapped.unique.human-viruse-checked.num-more_than_two.fa.fa','w')

while True:
    line1 = inFile.readline().strip()
    line2 = inFile.readline().strip()
    seq = line2
    if line1:
        fields = line1.split('\t')
        point = int(fields[-1]) - 1
        flag1 = 0
        flag2 = 0
        pep1 = []
        pep2 = []
        for i in range(point-1,-1,-1):
            if seq[i]!='K' and seq[i]!='R':
                pep1.append(seq[i])
            else:
                flag1 = 1
                break
        pep1 = pep1[::-1]
        for i in range(point,len(seq)):
            if seq[i]!='K' and seq[i]!='R':
                pep2.append(seq[i])
            else:
                flag2 = 1
                break
        pep2.append(seq[i])
        if flag1 ==1 and flag2 ==1:
            #ouFile.write(fields[0]+'\n')
            ouFile.write(''.join(pep1+pep2)+'\n')
    else:
        break
inFile.close()
ouFile.close()

