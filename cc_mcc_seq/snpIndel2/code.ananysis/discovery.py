import sys
fa=open(sys.argv[1],'r')
fb=open('%s.new'%sys.argv[1],'w')
fc=open('%s.known'%sys.argv[1],'w')
fd=open('%s.title'%sys.argv[1],'w')
fe=open('%s.stat'%sys.argv[1],'w')
row=0
known=0
new=0
while row<119 :
		line=fa.readline()
		fd.write(line)
		row=row+1
while True:
		line=fa.readline()
		if len(line)==0:
			break
		else:
			a=line.split('\t')
#				if a[2].find('rs')!=-1:
#	   			fb.write(line)
#				new=new+1
#			else:
#				fc.write(line)
#				known=known+1
			if a[2]=='.' :
				fb.write(line)
				new=new+1
			else :
				fc.write(line)
				known=known+1
fe.write('new snp:%d\n'%new)
fe.write('known snp:%d\n'%known)
fe.write('new/all: %f\n'%(new/(new+known)))
fe.write('known/all: %f\n'%(known/(new+known)))

		

 

  


