#### python neworknown.py raw.snp.vcf
#### python neworknown.py raw.snp.recalibrated.vcf
import sys
inFile1=open(sys.argv[1],'r')
#ouFile1=open('%s.new'%sys.argv[1],'w')
#ouFile2=open('%s.known'%sys.argv[1],'w')
#ouFile3=open('%s.title'%sys.argv[1],'w')
ouFile4=open('%s.stat'%sys.argv[1],'w')
row=0
known=0
new=0

if sys.argv[1].find('recalibrated')==-1 :
    for tmp in range(119) :
        line=inFile1.readline()
        #ouFile3.write(line)
    for line in inFile1 :
        fields=line.split('\t')
        if fields[2]=='.' :
    	#ouFile1.write(line)
            new=new+1
        else :
    	#ouFile2.write(line)
            known=known+1
    
    ouFile4.write('new snp:%d\n'%new)
    ouFile4.write('known snp:%d\n'%known)
    ouFile4.write('new/all: %f\n'%(new/(new+known)))
    ouFile4.write('known/all: %f\n'%(known/(new+known)))

if sys.argv[1].find('recalibrated')!=-1 :
    for tmp in range(125) :
        line=inFile1.readline()
        #ouFile3.write(line)
    for line in inFile1 :
        fields=line.split('\t')
        if fields[6] == 'PASS' :
            if fields[2]=='.' :
        	#ouFile1.write(line)
                new=new+1
            else :
        	#ouFile2.write(line)
                known=known+1
    
    ouFile4.write('new snp:%d\n'%new)
    ouFile4.write('known snp:%d\n'%known)
    ouFile4.write('new/all: %f\n'%(new/(new+known)))
    ouFile4.write('known/all: %f\n'%(known/(new+known)))


inFile1.close()
#ouFile1.close()
#ouFile2.close()
#ouFile3.close()
ouFile4.close()

		

 

  


