### ls *.jmp.txt |xargs -n 1 python 1.fa.py
import sys

D = dict()
inFile = open('/netshare1/home1/szzhongxin/proj1/hansun/viruses/'+ sys.argv[1].split('.')[0]+'.unmapped')
for line in inFile:
    line = line.strip()
    fields = line.split('\t')
    D.setdefault(fields[0], [])
    D[fields[0]].append(fields[9])
inFile.close()



inFile = open(sys.argv[1])
ouFile = open(sys.argv[1].split('.txt')[0] + '.fa', 'w')
ouFile2 = open(sys.argv[1].split('.txt')[0] + '.2.fa', 'w')
#D2 = dict()
if sys.argv[1].find('ICC4A')==0:
    for line in inFile:
        line = line.strip()
        fields = line.split()
        if fields:
            if fields[0].find('HWI') != -1 : 
                seq1 = fields[0]
                if fields[0].find('_')!=-1:
                    fs = seq1.split('_')
                    if fs[7] == '1':
                        seq2 = '_'.join(fs[0:8]+['2'])
                    elif fs[7] == '2':
                        seq2 = '_'.join(fs[0:8]+['1'])
                if fields[0].find(':') != -1: 
                    fs = seq1.split(':')
                    if fs[7] == '1':
                        seq2 = ':'.join(fs[0:7]+['2']+fs[8:10]+['#2'])
                    elif fs[7] == '2':
                        seq2 = ':'.join(fs[0:7]+['1']+fs[8:10]+['#1'])

                if seq1 in D and seq2 in D:
                    ouFile.write('>'+seq1 + '\n')
                    ouFile.write(D[seq1][0] + '\n')
                    ouFile.write('>'+seq2 + '\n')
                    ouFile.write(D[seq2][0] + '\n')



else:
    for line in inFile:
        line = line.strip()
        fields = line.split()
        if fields:
            if fields[0].find(':') != -1:
                seq1 = fields[0]
                fs = seq1.split(':')
                if sys.argv[1].split('.')[0] in ['CHC10A','ICC10A','ICC9A']:
                    if fs[7] == '1':
                        seq2 = ':'.join(fs[0:7]+['2']+fs[8:])
                    elif fs[7] == '2':
                        seq2 = ':'.join(fs[0:7]+['1']+fs[8:])
                    if seq1 in D and seq2 in D:
                        ouFile.write('>' + seq1 + '\n')
                        ouFile.write(D[seq1][0] + '\n')
                        ouFile.write('>' + seq2 + '\n')
                        ouFile.write(D[seq2][0] + '\n')
                elif sys.argv[1].split('.')[0] in ['CHC5A','CHC6A','CHC7A','ICC5A',]:
                    if fs[7] == '1':
                        seq2 = ':'.join(fs[0:7]+['2']+fs[8:10]+['#2'])
                    elif fs[7] == '2':
                        seq2 = ':'.join(fs[0:7]+['1']+fs[8:10]+['#1'])

                    if seq1 in D and seq2 in D:
                        ouFile.write('>' + seq1 + '\n')
                        ouFile.write(D[seq1][0] + '\n')
                        ouFile.write('>' + seq2 + '\n')
                        ouFile.write(D[seq2][0] + '\n')

                elif sys.argv[1].split('.')[0].find('B') != -1:
                    seq =seq1
                    #D2.setdefault(seq, 0)
                    #D2[seq] += 1
                    seq1 = seq + ':1'
                    seq2 = seq + ':2'

                    if seq in D :
                        if len(D[seq]) > 1:
                            ouFile.write('>' + seq1 + '\n')
                            ouFile.write(D[seq][0] + '\n')
                            ouFile.write('>' + seq2 + '\n')
                            ouFile.write(D[seq][1] + '\n')
                        else:
                            ouFile2.write('>' + seq1 + '\n')
                            ouFile2.write(D[seq][0] + '\n')


            #elif fields[0].find('_') != -1:
            #    seq1 = fields[0]
            #    fs = seq1.split('_')
            #    if sys.argv[1].split('.')[0] in ['ICC4A']:
            #        if fs[7] == '1':
            #            seq2 = '_'.join(fs[0:8]+['2'])
            #        elif fs[7] == '2':
            #            seq2 = '_'.join(fs[0:8]+['1'])
    


inFile.close()
ouFile.close()
ouFile2.close()
