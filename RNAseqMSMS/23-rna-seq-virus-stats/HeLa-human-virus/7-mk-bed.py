def mk_bed(inF,desc):
    I = 35
    n = 0
    inFile = open(inF)
    ouFile = open(inF+'.bed','w')
    ouFile.write('browser position '+desc+'\n')
    ouFile.write('track name="HPV18" description="HPV18 Integration" visibility=2 itemRgb="On"'+'\n')
    for line in inFile:
        n+=1
        line = line.strip()
        fields = line.split('\t')
        ch = fields[0]
        pos = int(fields[1])
        ouFile.write(fields[0]+'\t'+str(pos)+'\t'+str(pos+I)+'\t'+'pos'+str(n)+'\t'+'0'+'\t'+'+'+'\t'+str(pos)+'\t'+str(pos+I)+'\t'+'255,0,0'+'\n')
    inFile.close()
    ouFile.close()

mk_bed('ERR0498-04-05.unmapped.unique.human-viruse-checked-chr8-128230000-128250000-human-chr-site-unique','chr8:128230000-128250000')
