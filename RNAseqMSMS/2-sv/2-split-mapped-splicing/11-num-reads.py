'''
splicing reads:
    497949 + 275733
'''


def num(inF):
    D = {}
    inFile = open(inF)
    while True:
        line1 = inFile.readline().strip()
        line2 = inFile.readline().strip()
        if line1:
            fields = line1.split('\t')
            D[fields[0]]=1
        else:
            break
    inFile.close()
    print(len(D))

num('ERR0498-04-05.unmapped.unique.total.fasta.blated.filtered.seq1.splicing.known')
