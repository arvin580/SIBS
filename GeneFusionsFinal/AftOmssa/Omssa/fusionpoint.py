inFile1=open('/netshare1/home1/people/hansun/GeneFusions/AnnotatedProtein/ensemble_protein','r')
known=inFile1.read()
inFile1.close()

inFile1=open('/netshare1/home1/people/hansun/GeneFusions/AnnotatedProtein/uniprot_human','r')
known+=inFile1.read()
inFile1.close()

inFile1=open('/netshare1/home1/people/hansun/GeneFusions/ContaminatedProtein/contaminanted','r')
known+=inFile1.read()
inFile1.close()



import os
import re
files=os.listdir('.')
for file in files :
    if re.search('.out$',file) :
        inFile=open(file)
        ouFile=open(file+'.fusionpoint','w')
        inFile.readline()
        for line in inFile :
            line=line.strip()
            fields=line.split(',')
            start=int(fields[7])
            stop=int(fields[8])
            pep=fields[2]
            title=fields[9]
            if known.find(pep)==-1 :
                if title.find('genefusions')!=-1:
                    title1=title.split('&')[0]
                    title11=title1.split('|')
                    if len(title11)==7 :
                        point=int(title11[-2])
                        if start+2<=point<=stop-3 :
                            ouFile.write(line+'\n')
    


        inFile.close()
        ouFile.close()



for file in files :
    if re.search('.out$',file) :
        inFile=open(file)
        ouFile=open(file+'.splicingpoint','w')
        inFile.readline()
        for line in inFile :
            line=line.strip()
            fields=line.split(',')
            start=int(fields[7])
            stop=int(fields[8])
            pep=fields[2]
            title=fields[9]
            if known.find(pep)==-1 :
                if title.find('splicing')!=-1:
                    title1=title.split('&')[0]
                    title11=title1.split('|')
                    if len(title11)==7 :
                        point=int(title11[-2])
                        if start+2<=point<=stop-3 :
                            ouFile.write(line+'\n')
    


        inFile.close()
        ouFile.close()
