import subprocess
import os


mapped_both_flags = [83, 99, 147, 163]
mapped_wrong_insertsize = [81, 161, 97, 145, 65, 129, 113, 177]
chrs = ['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14',
                'chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX','chrY','chrM']

class StructuralVariation():
    def __init__(self, bam, ref):
        self.bam = bam
        self.bam_unmapped = bam + '.unmapped'
        self.ref = ref
        #self._bam_unmapped()
        self.translocation_paired()

    def translocation_paired(self):
        self._bam_mapped_wrong_insertsize()
        self._bam_trans()
    def inversion_paired(self):
        pass

    def duplication_paired(self):
        pass

    def deletion_paired(self):
        pass

    def _bam_mapped_wrong_insertsize(self):
        bam_mapped_wrong_insertsize = self.bam_unmapped + '.mapped_wrong_insertsize'
        inFile = open(self.bam_unmapped)
        ouFile = open(bam_mapped_wrong_insertsize, 'w')
        for line in inFile:
            fields = line.split('\t')
            if int(fields[1]) in mapped_wrong_insertsize and fields[2] in chrs:
                ouFile.write(line)
        inFile.close()
        ouFile.close()

    def _bam_trans(self):

    def _bam_unmapped(self):
        if self.bam.find('.bam') != -1:
            ouFile = open(self.bam_unmapped, 'w')
            sp=subprocess.Popen(['samtools','view',self.bam], stdout = subprocess.PIPE)
            for line in sp.stdout:
                fields = line.split('\t')
                if int(fields[1]) not in mapped_both_flags:
                    ouFile.write(line)
            ouFile.close()

        elif self.bam.find('.sam')!= -1:
            inFile = open(self.bam)
            ouFile = open(self.bam_unmapped, 'w')
            for line in inFile:
                if line.find('@') != 0  :
                    fields = line.split('\t')
                    if int(fields[1]) not in mapped_both_flags:
                        ouFile.write(line)
            inFile.close()
            ouFile.close()
        else:
            print('The input file seems not in bam or sam format!')
            return

