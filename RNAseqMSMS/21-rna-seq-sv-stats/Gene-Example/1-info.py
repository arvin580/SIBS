inFile = open('Gene-Example-MYC')
ouFile = open('Gene-Example-MYC-info','w')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    gene = ':'.join(fields[0].split(':')[1:])
    tp = fields[0].split('.')[0].split('-')[-1]
    num = fields[2]
    seq = fields[29].split('|')[0]

    ch1 = fields[6]
    start1_query = int(fields[11])
    end1_query = int(fields[12])
    start1_subject = int(fields[13])
    end1_subject = int(fields[14])

    ch2 = fields[18]
    start2_query= int(fields[23])
    end2_query=int(fields[24])
    start2_subject = int(fields[25])
    end2_subject = int(fields[26])


    if start1_subject < end1_subject and start2_subject < end2_subject:
        strand1 = '+'
        strand2 = '+'
    elif start1_subject < end1_subject and start2_subject >= end2_subject:
        strand1 = '+'
        strand2 = '-'
    elif start1_subject >= end1_subject and start2_subject < end2_subject:
        strand1 = '-'
        strand2 = '+'
    elif start1_subject >= end1_subject and start2_subject >= end2_subject:
        strand1='-'
        strand1='-'

    if (start1_query+end1_query)<(start2_query+start2_query):
        info = [tp,num,gene,ch1,strand1,start1_query,end1_query,start1_subject,end1_subject,ch2,strand2,start2_query,end2_query,start2_subject,end2_subject,seq]
    else:
        info = [tp,num,gene,ch2,strand2,start2_query,end2_query,start2_subject,end2_subject,ch1,strand1,start1_query,end1_query,start1_subject,end1_subject,seq]

    print('\t'.join([str(x) for x in info]))

 
inFile.close()
ouFile.close()
