inFile = open('/fs01/szzhongxin/proj1/hansun/RNAseq/result.txt')
L = []
for line in inFile:
    line = line.strip()
    fields = line.split()
    L.append(fields)
inFile.close()


score = 5000
def sv(inF):
    inFile = open(inF)
    for line in inFile:
        fields = line.split()
        fds = fields[0].split(':')
        gene = fds[0]
        sample = fds[1]
        ch = fds[2]
        start = int(fds[3])
        end = int(fds[4])


        for item in L:
            if item[2]==ch and item[5]==ch:
                if int(item[3])-score <= start <= int(item[3])+score or int(item[6])-score <= start <= int(item[6])+score \
                        or int(item[3])-score <= end <= int(item[3])+score or int(item[6])-score <= end <= int(item[6])+score :
                            print(line)
                            print(item)

    inFile.close()
def sv2(inF):
    inFile = open(inF)
    for line in inFile:
        fields = line.split()
        fds = fields[0].split(':')
        gene1 = fds[0]
        gene2 = fds[1]
        sample = fds[2]
        ch1 = fds[3]
        start = int(fds[4])
        ch2 = fds[5]
        end = int(fds[6])


        for item in L:
            if (item[2]==ch1 and item[5]==ch2) or (item[2]==ch2 and item[5]==ch1):
                if int(item[3])-score <= start <= int(item[3])+score or int(item[6])-score <= start <= int(item[6])+score \
                        or int(item[3])-score <= end <= int(item[3])+score or int(item[6])-score <= end <= int(item[6])+score :
                            print(line)
                            print(item)

    inFile.close()


sv('20s.delition.gene.reads.formated')
sv('20s.inversion.gene.reads.formated')
sv2('20s.translocation.gene.reads.formated')

