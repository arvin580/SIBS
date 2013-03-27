from xml.etree.ElementTree import *
import os

ouFile=open('tandem.peptides','w')
dir='.'
for f in os.listdir(dir) :
    file=dir+os.sep+f
    if file[-6:]=='.t.xml' :
        tree = ElementTree()
        tree.parse(file)
        group=tree.findall('group')
        for item in group :
            if item.get('id') :
                seq=[]
                mgf=[]
                label=[]
                info=[]
                pep = []

                b=item.findall('protein')
                for it in b :
                    label.append(it.get('label'))

                p=item.findall('protein/peptide')
                for it in p :
                    pep.append(''.join(it.text.strip().split()))

                s=item.findall('protein/peptide/domain')
                for it in s :
                    seq.append(it.get('seq'))
                    info.append(it.get('start')+':'+it.get('end')+':'+it.get('expect')+':'
                            +it.get('hyperscore')+':'+it.get('pre')+':'+it.get('post'))

                m=item.findall('group/note')
                for it in m :
                    mgf.append(it.text.strip())
        
                #ouFile.write(f+'\t'+'\t'.join(mgf)+'\t'+'\t'.join(seq)+'\n')
                #ouFile.write(f+'\t'+'\t'.join(label)+'\t'+'\t'.join(info)+'\t'+'\t'.join(seq)+'\n')

                if len(mgf)==1 and len(seq)==len(pep)==len(label)==len(info):
                    ouFile.write(f+'\t'+'\t'.join(mgf)+'\t')
                    for i in range(len(seq)):
                        ouFile.write(seq[i]+'\t')
                        ouFile.write(pep[i]+'\t')
                        ouFile.write(label[i]+'\t')
                        ouFile.write(info[i]+'\t')
                    ouFile.write('\n')
                else:
                    print('>'+ f )
                    print(mgf)
                    print(seq)
                    print(pep)
                    print(label)
                    print(info)
ouFile.close()
