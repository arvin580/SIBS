### python  5.cnv-multi.py *depth_1.5_upped_down_gene
import sys


D = {}
for inF in sys.argv[1:]:
    sample = inF.split('.')[1]
    inFile = open(inF)
    for line in inFile:
        line = line.strip()
        fields = line.split('\t')
        D.setdefault(fields[0], {})
        D[fields[0]][sample] = 1
    inFile.close()

#ouFile = open('5.'+'.'.join(sys.argv[1].split('.')[2:]), 'w')
ouFile = open('5.'+'varScan.copynumber.called.depth_'+sys.argv[1].split('_')[1]+'_upper_down_gene', 'w')
L = []
for k in D:
    ouFile.write(k+'\t'+str(D[k].get('ICC4',0))+'\t'+str(D[k].get('ICC5',0))+'\t'+str(D[k].get('ICC9',0))+
        '\t'+str(D[k].get('ICC10',0))+'\t'+
        str(D[k].get('CHC5',0))+'\t'+str(D[k].get('CHC6',0))+'\t'+str(D[k].get('CHC7',0))+'\t'+str(D[k].get('CHC10',0))+'\n')
        

    

