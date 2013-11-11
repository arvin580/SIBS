### python 2.human.py  uniprot_sprot_2013_11_11.fa
import sys
inFile = open(sys.argv[1])
ouFile = open('human_' + sys.argv[1] , 'w')
while True:
    head = inFile.readline()
    seq = inFile.readline()
    if head:
        if head.find('Homo sapiens')!=-1 or head.find('human')!=-1 :
            ouFile.write(head)
            ouFile.write(seq)

    else:
        break
inFile.close()
ouFile.close()
