from xml.etree.ElementTree import *
import os

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


#ouFile=open('tandem.peptides3','w')
dir='.'
for f in os.listdir(dir) :
    fe=dir+os.sep+f
    #if fi[-6:]=='.t.xml' :
    #if f == '20090815_Velos1_NaNa_SA_10k_Hela_Trypsin_SECC_SAXpH_11.2013_03_27_14_04_16.t.xml':
    if f == 'test-xml':
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
                        pe = Peptide()
                        pe.seq = y.get('seq')
                        pe.attr = y.get('start')+':'+y.get('end')+':'+y.get('expect')+':'\
                                +y.get('hyperscore')+':'+y.get('pre')+':'+y.get('post')
                        p.peptide.append(pe)
                    Spec.protein.append(p)

                print(Spec.name+'\t'),
                print(len(Spec.protein))
                for protein in Spec.protein:
                    for peptide in protein.peptide:
                        print(protein.name+'\t'+peptide.seq+'\t'+peptide.attr+'\t'),
                        #print(peptide.seq+'\t'+peptide.attr+'\t'),
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
