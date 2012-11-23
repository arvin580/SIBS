from xml.etree.ElementTree import *
import os
'''
ouFile=open('pep2mgf_liuxiaohui','w')
dir='/netshare1/home1/people/hansun/Project/fudancls/Tandem/output'
for f in os.listdir(dir) :
    file=dir+os.sep+f
    if file[-4:]=='.xml' :
        tree = ElementTree()
        tree.parse(file)
        group=tree.findall('group')
        for item in group :
            if item.get('id') :
                seq=[]
                mgf=[]
                s=item.findall('protein/peptide/domain')
                for it in s :
                    seq.append(it.get('seq'))
                m=item.findall('group/note')
                for it in m :
                    mgf.append(it.text.strip())
        
                ouFile.write(f+'\t'+'\t'.join(mgf)+'\t'+'\t'.join(seq)+'\n')
ouFile.close()
'''

ouFile=open('pep2mgf_chenchen','w')
dir='/netshare1/home1/people/hansun/Project/fudancls/Tandem/output2'
for f in os.listdir(dir) :
    file=dir+os.sep+f
    if file[-4:]=='.xml' :
        tree = ElementTree()
        tree.parse(file)
        group=tree.findall('group')
        for item in group :
            if item.get('id') :
                seq=[]
                mgf=[]
                s=item.findall('protein/peptide/domain')
                for it in s :
                    seq.append(it.get('seq'))
                m=item.findall('group/note')
                for it in m :
                    mgf.append(it.text.strip())
        
                ouFile.write(f+'\t'+'\t'.join(mgf)+'\t'+'\t'.join(seq)+'\n')
ouFile.close()
