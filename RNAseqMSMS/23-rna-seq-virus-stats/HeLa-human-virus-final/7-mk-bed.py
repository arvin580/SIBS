POS = sorted([128241377,128231055,128241548,
        128231213,128241370,128230632,128235913
        ])

def mk_bed(desc):
    I = 20
    n = 0
    ouFile = open('HeLa-chr8-Integration.bed','w')
    ouFile.write('browser position '+desc+'\n')
    ouFile.write('track name="HPV-18" description="HPV-18 Integration" visibility=2 itemRgb="On"'+'\n')
    for pos in POS:
        n+=1
        ch = 'chr8'
        ouFile.write(ch+'\t'+str(pos)+'\t'+str(pos+I)+'\t'+'chr8:'+str(pos)+'\t'+'0'+'\t'+'+'+'\t'+str(pos)+'\t'+str(pos+I)+'\t'+'255,0,0'+'\n')
    ouFile.close()

mk_bed('chr8:128230000-128250000')
