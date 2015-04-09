## python known_new.py raw.snp.recalibrated.annovar.exonic_variant_function raw.snp.recalibrated.new.annovar.exonic_variant_function raw.snp.recalibrated.known.annovar.exonic_variant_function  raw.snp.recalibrated.annovar.exonic_variant_function.stat
import sys
fa=open(sys.argv[1],'r')
fb=open(sys.argv[2],'w')
fc=open(sys.argv[3],'w')
fe=open(sys.argv[4],'w')

known=0
new=0
while True:
		line=fa.readline()
		if len(line)==0:
			break
		else:
			a=line.split('\t')
			if a[7]=='.' :
				fb.write(line)
				new=new+1
			else :
				fc.write(line)
				known=known+1
fe.write('new snp:%d\n'%new)
fe.write('known snp:%d\n'%known)
fe.write('new/all: %f\n'%(new/(new+known)))
fe.write('known/all: %f\n'%(known/(new+known)))
fa.close()
fb.close()
fc.close()
fe.close()
		

 

  


