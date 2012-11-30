import subprocess
import os

###prerequired: samtools, bowtie, blat


mapped_both_flags = [83, 99, 147, 163]
mapped_wrong_insertsize = [81, 161, 97, 145, 65, 129, 113, 177]
chrs = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8',
        'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16',
        'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22',
        'chrX', 'chrY', 'chrM']


class StructuralVariation():
    def __init__(self, bam, ref):
        self.bam = bam
        self.bam_unmapped = bam + '.unmapped'
        self.ref = ref
        #self._bam_unmapped()
        self.bam_mapped_wrong_insertsize = self.bam_unmapped + '.mapped_wrong_insertsize'
        self.trans = self.bam_unmapped + '.trans'
        self.trans_fq1 = self.trans + '.read1.fq'
        self.trans_fq2 = self.trans + '.read2.fq'
        self.translocation_paired()

    def translocation_paired(self):
        self._bam_mapped_wrong_insertsize()
        self._bam_trans()
        self._mk_fq()

    def inversion_paired(self):
        pass

    def duplication_paired(self):
        pass

    def deletion_paired(self):
        pass

    def _mk_fq(self):
        inFile = open(self.trans)
        ouFile1 = open(self.trans_fq1, 'w')
        ouFile2 = open(self.trans_fq2, 'w')
        while True:
            line1 = inFile.readline()
            line2 = inFile.readline()
            if line1:
                line1s = line1.split('\t')
                line2s = line2.split('\t')
                ouFile1.write('@' + line1s[0] + '\n')
                ouFile1.write(line1s[9] + '\n')
                ouFile1.write('+'+'\n')
                ouFile1.write('H'*len(line1s[9])+'\n')
                ouFile2.write('@' + line2s[0] + '\n')
                ouFile2.write(line2s[9] + '\n')
                ouFile2.write('+'+'\n')
                ouFile2.write('H'*len(line2s[9])+'\n')
            else:
                break

        inFile.close()
        ouFile1.close()
        ouFile2.close()

    def _bam_mapped_wrong_insertsize(self):
        inFile = open(self.bam_unmapped)
        ouFile = open(self.bam_mapped_wrong_insertsize, 'w')
        for line in inFile:
            fields = line.split('\t')
            if int(fields[1]) in mapped_wrong_insertsize and fields[2] in chrs:
                ouFile.write(line)
        inFile.close()
        ouFile.close()

    def _bam_trans(self):
        inFile = open(self.bam_mapped_wrong_insertsize)
        ouFile = open(self.trans, 'w')
        D = {}
        sep = ':'
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            try:
                if fields[0].find(':') != -1:
                    k = ':'.join(fields[0].split(':')[0:7])
                elif fields[0].find('_') != -1:
                    k = '_'.join(fields[0].split('_')[0:7])
                    sep = '_'
                else:
                    raise 
                D.setdefault(k, [])
                D[k].append('\t'.join(fields[1:]))
            except:
                print("Reads name related problem")
                return
        for k in D:
            if len(D[k]) == 2:
                if D[k][0].split('\t')[1] != D[k][1].split('\t')[1]:
                    ouFile.write(k + sep + '1' + '\t' + D[k][0] + '\n')
                    ouFile.write(k + sep + '2' + '\t' + D[k][1] + '\n')


        inFile.close()
        ouFile.close()

    def _bam_unmapped(self):
        if self.bam.find('.bam') != -1:
            ouFile = open(self.bam_unmapped, 'w')
            sp = subprocess.Popen(['samtools', 'view', self.bam], stdout=subprocess.PIPE, buffersize=1)
            for line in sp.stdout:
                fields = line.split('\t')
                if int(fields[1]) not in mapped_both_flags:
                    ouFile.write(line)
            ouFile.close()
        elif self.bam.find('.sam') != -1:
            inFile = open(self.bam)
            ouFile = open(self.bam_unmapped, 'w')
            for line in inFile:
                if line.find('@') != 0:
                    fields = line.split('\t')
                    if int(fields[1]) not in mapped_both_flags:
                        ouFile.write(line)
            inFile.close()
            ouFile.close()
        else:
            print('The input file seems not in bam or sam format!')
            return
