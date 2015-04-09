fa=open('raw.snp.vcf','r')
fb=open('haha.vcf','w')
row=0
while row<120 :
		line=fa.readline()
		row=row+1
while True:
		line=fa.readline()
		if len(line)==0:
			break
		else:
			a=line.split('\t')
			if a[2].find('rs')!=-1:
				fb.write(line)
		

 

  


