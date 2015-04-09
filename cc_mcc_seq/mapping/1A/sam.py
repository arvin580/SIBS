'''
import pysam
samfile = pysam.Samfile( "1A.bam", "rb" )
for alignedread in samfile.fetch('chr1', 100000, 100100):
    print alignedread
samfile.close()
'''
import pysam
samfile = pysam.Samfile("1A.bam", "rb" )
for pileupcolumn in samfile.pileup( 'chr1', 100000, 100100):
    #print
    print 'coverage at base %s = %s' % (pileupcolumn.pos , pileupcolumn.n)
    for pileupread in pileupcolumn.pileups:
        #print '\tbase in read %s = %s' % (pileupread.alignment.qname, pileupread.alignment.seq[pileupread.qpos])
        print pileupread.alignment.seq[pileupread.qpos]

samfile.close()
