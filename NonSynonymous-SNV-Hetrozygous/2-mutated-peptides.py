import re
import sys
### acid variation caused by non-synonymous SNV
SNV = {}
SNV['A'] = ['E', 'D', 'G', 'P', 'S', 'T', 'V']
SNV['C'] = ['G', 'F', '*', 'S', 'R', 'W', 'Y']
SNV['E'] = ['A', 'D', 'G', 'K', '*', 'Q', 'V']
SNV['D'] = ['A', 'E', 'G', 'H', 'N', 'V', 'Y']
SNV['G'] = ['A', 'C', 'E', 'D', '*', 'S', 'R', 'W', 'V']
SNV['F'] = ['C', 'I', 'L', 'S', 'V', 'Y']
### remove I to L
SNV['I'] = ['F', 'K', 'M', 'N', 'S', 'R', 'T', 'V']
SNV['H'] = ['D', 'L', 'N', 'Q', 'P', 'R', 'Y']
SNV['K'] = ['E', 'I', '*', 'M', 'N', 'Q', 'R', 'T']
SNV['M'] = ['I', 'K', 'L', 'R', 'T', 'V']
### remove L to I
SNV['L'] = ['F', 'H', '*', 'M', 'Q', 'P', 'S', 'R', 'W', 'V']
SNV['N'] = ['D', 'I', 'H', 'K', 'S', 'T', 'Y']
SNV['Q'] = ['E', 'H', 'K', '*', 'L', 'P', 'R']
SNV['P'] = ['A', 'H', 'L', 'Q', 'S', 'R', 'T']
SNV['S'] = ['A', 'C', 'G', 'F', 'I', '*', 'L', 'N', 'P', 'R', 'T', 'W', 'Y']
SNV['R'] = ['C', 'G', 'I', 'H', 'K', '*', 'M', 'L', 'Q', 'P', 'S', 'T', 'W']
SNV['T'] = ['A', 'I', 'K', 'M', 'N', 'P', 'S', 'R']
SNV['W'] = ['C', 'G', '*', 'L', 'S', 'R']
SNV['V'] = ['A', 'E', 'D', 'G', 'F', 'I', 'M', 'L']
SNV['Y'] = ['C', 'D', 'F', 'H', '*', 'N', 'S']

D = {}
try:
    inFile = open('human_uniprot_sprot_2013_11_11_reversed.fa')
    while True:
        head = inFile.readline().strip()
        seq = inFile.readline().strip()
        if head:
            if head.find('REVERSE') == -1:
                D[head[1:]] = seq
        else:
            break
    inFile.close()
except:
    pass

inFile = open('Peptides-Identified-First')
ouFile = open('Peptides-Identified-First-Mutated.fa', 'w')
while True:
    head = inFile.readline().strip()
    seq = inFile.readline().strip()
    if head:
        for i in range(len(seq)): 
            if i != len(seq) - 1:
                for x in SNV[seq[i]]:
                    if x != 'K' and x != 'R' and x != '*':
                        seq2 = seq[0:i] + x + seq[i + 1:] 
                        ouFile.write(head + ' '+seq+' ' + 'VARIATION-Normal:' + str(i+1) + ':' + seq[i] + ':' + x + '\n' )
                        ouFile.write(seq2 + '\n')
                    elif x == 'K' or x == 'R' :
                        seq2 = seq[0:i] + x
                        if len(seq2) >= 6:
                            ouFile.write(head + ' '+seq+' ' + 'VARIATION-KR:' + str(i+1) + ':' + seq[i] + ':' + x + '\n' )
                            ouFile.write(seq2 + '\n')
                    elif x == '*':
                        seq2 = seq[0:i]
                        if len(seq2) >= 6:
                            ouFile.write(head + ' '+seq+' ' + 'VARIATION-StopGain:' + str(i+1) + ':' + seq[i] + ':' + x + '\n' )
                            ouFile.write(seq2 + '\n')
            else:
                for x in SNV[seq[i]]:
                    if x == 'K' or x == 'R':
                        seq2 = seq[0:i] + x
                        if len(seq2) >= 6:
                            ouFile.write(head + ' '+seq+' ' + 'VARIATION-Terminal-KR:' + str(i+1) + ':' + seq[i] + ':' + x + '\n' )
                            ouFile.write(seq2 + '\n')
                    elif x == '*':
                        seq2 = seq[0:i]
                        if len(seq2) >= 6:
                            ouFile.write(head + ' '+seq+' ' + 'VARIATION-Terminal-StopGain:' + str(i+1) + ':' + seq[i] + ':' + x + '\n' )
                            ouFile.write(seq2 + '\n')
                    else:
                        h = head.split('\t')[0][1:]
                        if h in D:
                            protein = D[h]
                            s = re.search('%s(.*?[KR])'%seq, protein)
                            if s:
                                seq2 = seq[0:i] + x + s.group(1)
                                ouFile.write(head + ' '+seq+' ' + 'VARIATION-Terminal-Normal1' + str(i+1) + ':' + seq[i] + ':' + x + '\n' )
                                ouFile.write(seq2 + '\n')
                            else:
                                s = re.search('%s(.*?$)'%seq, protein)
                                if s:
                                    seq2 = seq[0:i] + x + s.group(1)
                                    ouFile.write(head + ' '+seq+' ' + 'VARIATION-Terminal-Normal2' + str(i+1) + ':' + seq[i] + ':' + x + '\n' )
                                    ouFile.write(seq2 + '\n')
    else:
        break

inFile.close()
ouFile.close()
