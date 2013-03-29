from xml.etree.ElementTree import *
import sys

class Spectrum:
    name = ''
    protein = []
class Protein:
    name = ''
    seq = ''
    attr = ''
    peptide = []
class Peptide:
    seq = ''
    attr = ''


inF = sys.argv[1]
ouFile = open(sys.argv[1]+'.txt','w')
tree = ElementTree()
tree.parse(fe)
group=tree.findall('group')
for item in group :
    if item.get('id') :
        Spec = Spectrum()
        s = item.findall('group/note')
        if len(s) == 1:
            Spec.name = s[0].text
        else:
            print('spec error')

        pro=item.findall('protein')
        for x in pro :
            p = Protein()
            s = x.findall('note')
            if len(s)==1:
                p.name=s[0].text
            else:
                print('protein error')
            pep = x.findall('peptide/domain')
            for y in pep:
                print('xx')
                pe = Peptide()
                pe.seq = y.get('seq')
                pe.attr = y.get('start')+':'+y.get('end')+':'+y.get('expect')+':'\
                        +y.get('hyperscore')+':'+y.get('pre')+':'+y.get('post')
                p.peptide.append(pe)
            Spec.protein.append(p)
        print('###')
        print(len(Spec.protein))
        for x in Spec.protein:
            print(len(x.peptide))
        print('###')

        print(Spec.name+'\t'),
        for protein in Spec.protein:
            for peptide in protein.peptide:
                #print(protein.name+'\t'+peptide.seq+'\t'+peptide.attr+'\t'),
                #print(peptide.seq+'\t'+peptide.attr+'\t'),
                print(protein.name[0:7]+'\t'+peptide.seq+'\t'),
        print('\n'),
        '''

        p=item.findall('protein/peptide')
        for it in p :
            pep.append(''.join(it.text.strip().split()))

        s=item.findall('protein/peptide/domain')
        for it in s :
            seq.append(it.get('seq'))
            info.append(it.get('start')+':'+it.get('end')+':'+it.get('expect')+':'
                    +it.get('hyperscore')+':'+it.get('pre')+':'+it.get('post'))


        #ouFile.write(f+'\t'+'\t'.join(mgf)+'\t'+'\t'.join(seq)+'\n')
        #ouFile.write(f+'\t'+'\t'.join(label)+'\t'+'\t'.join(info)+'\t'+'\t'.join(seq)+'\n')

        if len(mgf)==1 and len(seq)==len(pep)==len(pro)==len(info):
            ouFile.write(f+'\t'+'\t'.join(mgf)+'\t')
            for i in range(len(seq)):
                ouFile.write(seq[i]+'\t')
                ouFile.write(pep[i]+'\t')
                #ouFile.write(label[i]+'\t')
                ouFile.write(pro[i]+'\t')
                ouFile.write(info[i]+'\t')
            ouFile.write('\n')
        else:
            print('>'+ f )
            print(mgf)
            print(seq)
            print(pep)
            print(label)
            print(info)
        '''
