import subprocess
mapped_flags = [83, 99, 147, 163]

class StructuralVariation():
    def __init__(self, bam, ref):
        self.bam = bam
        self.bam_unmapped = bam + '.unmapped'
        self.ref = ref
        self._bam_unmapped()

    def translocation(self):
        pass

    def inversion(self):
        pass

    def duplication(self):
        pass

    def deletion(self):
        pass

    def _bam_unmapped(self):
        if self.bam.find('.bam') != -1:
            ouFile = open(self.bam_unmapped, 'w')
            sp=subprocess.Popen(['samtools','view',self.bam], stdout = subprocess.PIPE)
            for line in sp.stdout:
                fields = line.split('\t')
                if int(fields[1]) not in mapped_flags:
                    ouFile.write(line)
            ouFile.close()

        elif self.bam.find('.sam')!= -1:
            inFile = open(self.bam)
            ouFile = open(self.bam_unmapped, 'w')
            for line in inFile:
                fields = line.split('\t')
                if int(fields[1]) not in mapped_flags:
                    ouFile.write(line)
            inFile.close()
            ouFile.close()
        else:
            print('The input file seems not in bam or sam format!')
            return

