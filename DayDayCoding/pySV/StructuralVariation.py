import subprocess
import os

###prerequired: samtools, bowtie, blat


mapped_both_flags = [83, 99, 147, 163]
mapped_wrong_insertsize = [81, 161, 97, 145, 65, 129, 113, 177]
bowtie_sigle_unmapped = [4]
chrs = ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8',
        'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16',
        'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22',
        'chrX', 'chrY', 'chrM']


class StructuralVariation():
    def __init__(self, bam, ref, bowtie_index):
        self.bam = bam
        self.bam_unmapped = bam + '.unmapped'
        self.ref = ref
        if bowtie_index:
            self.bowtie_index = bowtie_index
        else:
            self.bowtie_index = os.path.split(self.ref)[1]
            self._bowie_index()
        #self._bam_unmapped()


        self.bam_mapped_wrong_insertsize = self.bam_unmapped + '.mapped_wrong_insertsize'
        self.trans = self.bam_unmapped + '.trans'
        self.trans_fq = self.trans + '.fq'
        self.trans_sam = self.trans + '.sam'
        self.trans_paired = self.trans + '.paired'

        self.translocation_paired()

    def translocation_paired(self):
        self._bam_mapped_wrong_insertsize()
        self._bam_trans()
        self._mk_fq()
        self._bowtie()
        self._bowtie_unique(self.trans_sam)
        self._unique_paired()

    def inversion_paired(self):
        pass

    def duplication_paired(self):
        pass

    def deletion_paired(self):
        pass

    def _bowie_index(self):
        sp = subprocess.call(['bowtie-build', self.ref, self.bowtie_index])

    def _bowtie(self):
        sp = subprocess.call(['bowtie', '-k 3' , '-S', self.bowtie_index, self.trans_fq, self.trans_sam])
    
    def _bowtie_unique(self, inF):
        inFile = open(inF)
        self.bowtie_unique = inF + '.unique'
        ouFile = open(self.bowtie_unique, 'w')
        D = {}
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            if len(fields) > 10:
                D.setdefault(fields[0], [])
                if not D[fields[0]]:
                    D[fields[0]].append(line)
                else:
                    D[fields[0]].append([])
                
        inFile.close()
        for k in D:
            if len(D[k]) == 1 and int(D[k][0].split('\t')[1]) not in bowtie_sigle_unmapped:
                ouFile.write(D[k][0] + '\n')
        ouFile.close()
    
    def _unique_paired(self):
        inFile = open(self.bowtie_unique)
        ouFile = open(self.trans_paired, 'w')
        D = {}
        for line in inFile:
            line = line.strip()
            fields = line.split('\t')
            if fields[2] in chrs:
                readname_key, seq = self._readname_key(fields[0])
                D.setdefault(readname_key, [])
                D[readname_key].append(line)
        inFile.close()
        
        for k in D : 
            if len(D[k]) == 2:
                for item in D[k]:
                    ouFile.write(item + '\n')
        ouFile.close()

        self._remove_tmp_file()
    
    def _remove_tmp_file(self):
        os.remove(self.bam_mapped_wrong_insertsize)
        os.remove(self.trans)
        os.remove(self.trans_fq)
        os.remove(self.trans_sam)
        os.remove(self.bowtie_unique)

    def _mk_fq(self):
        inFile = open(self.trans)
        ouFile = open(self.trans_fq, 'w')
        for line in inFile:
            fields = line.split('\t')
            ouFile.write('@' + fields[0] + '\n')
            ouFile.write(fields[9] + '\n')
            ouFile.write('+'+'\n')
            ouFile.write('H'*len(fields[9])+'\n')
        inFile.close()
        ouFile.close()

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
            readname_key, sep = self._readname_key(fields[0])
            D.setdefault(readname_key, [])
            D[readname_key].append('\t'.join(fields[1:]))
        for k in D:
            if len(D[k]) == 2:
                if D[k][0].split('\t')[1] != D[k][1].split('\t')[1]:
                    ouFile.write(k + sep + '1' + '\t' + D[k][0] + '\n')
                    ouFile.write(k + sep + '2' + '\t' + D[k][1] + '\n')


        inFile.close()
        ouFile.close()

    def _readname_key(self, readname):
        '''
        return read_name_key and sep
        '''
        try:
            sep = ':'
            if readname.find(sep) != -1:
                k = sep.join(readname.split(sep)[0:7])
            elif readname.find('_') != -1:
                sep = '_'
                k = sep.join(readname.split(sep)[0:7])
            else:
                raise 
            return [k, sep]
        except:
            print("Reads name related problem")
            return


    def _bam_unmapped(self):
        if self.bam.find('.bam') != -1:
            ouFile = open(self.bam_unmapped, 'w')
            sp = subprocess.call(['samtools', 'view', self.bam], stdout=subprocess.PIPE, bufsize=1)
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
