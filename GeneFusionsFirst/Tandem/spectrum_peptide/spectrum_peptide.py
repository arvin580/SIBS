#!/usr/bin/python

### python spectrum_peptide.py /netshare1/home1/people/hansun/GeneFusions/Tandem/output /netshare1/home1/people/hansun/GeneFusions/Tandem/output2 spectrum_peptide_map spectrum_peptide_map2 

import os
import sys
import re

inDir1=sys.argv[1]
inDir2=sys.argv[2]
ouFile1=sys.argv[3]
ouFile2=sys.argv[4]

peptide=[]
dict1={}
dict2={}

ouFileA=open(ouFile1,'w')


for file in os.listdir(inDir1) :
	if file.find('.xml') != -1 :
		inFileA=open(inDir1+'/'+file)
		for line in inFileA :
			m=re.search(r'seq="(\w+)"',line) 
			if m :
				peptide.append(m.group(1))
			m=re.search(r'<note label="Description">(.*dta)',line) 
			if m :
				dict1[m.group(1)]=set(peptide)
				peptide=[]
		inFileA.close()
for key in dict1 :
	ouFileA.write(key+'\t'+'\t'.join(dict1[key])+'\n')

ouFileA.close()



ouFileA=open(ouFile2,'w')
		
for file in os.listdir(inDir2) :
	if file.find('.xml') != -1 :
		inFileA=open(inDir2+'/'+file)
		for line in inFileA :
			m=re.search(r'seq="(\w+)"',line) 
			if m :
				peptide.append(m.group(1))
			m=re.search(r'<note label="Description">(.*dta)',line) 
			if m :
				dict2[m.group(1)]=set(peptide)
				peptide=[]
		inFileA.close()
for key in dict2 :
	ouFileA.write(key+'\t'+'\t'.join(dict2[key])+'\n')

ouFileA.close()


