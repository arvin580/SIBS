#! /usr/bin/env python
from optparse import OptionParser
import urllib
import time
import os
UNIPROT = 'http://www.uniprot.org/uniprot'


def main():
    version = '%prog 1.0'
    parser = OptionParser(version=version)
    parser.add_option('-a', '--accession', action='store', type='string',
                      dest='accession',
                      help='the uniprot proteion accession number \
                            or ID (AC/ID, such like P15311 or EZRI_HUMAN)')
    parser.add_option('-f', '--file', action='store',
                      type='string', dest='file',
                      help='the protein sequence file in fasta format')
    parser.add_option('-s', '--sequence', action='store', type='string',
                      dest='sequence',
                      help='the protein acid sequence, requiring -o')
    parser.add_option('-l', '--length', action='store', type='int',
                      dest='length', default=100,
                      help='the shortest sequence length, \
                            default value is 100')
    parser.add_option('-o', '--output', action='store', type='string',
                      dest='output', help='The output file in fasta format, \
                              the default name for -a is ACCESSION.fasta, \
                              and the default name for -f is FILE.fasta. \
                              Start and End point were \
                              added to the head line, \
                              Eg, in ">sp|P15311-1-586|EZRI_HUMAN-1-586", \
                              start point is 1 and end point is 586')
    (options, args) = parser.parse_args()
    if options.length <= 0:
        print('Warning: The specified sequence lenght must be positive')
        exit()
    if (options.accession and options.file) or \
       (options.accession and options.sequence) or \
       (options.file and options.sequence):
        print('Warning: only specify one among the -a, -f and -s options')
        exit()
    #try:
    truncating(options)
    #except:
    #    pass


def truncating(options):
    if options.accession:
        URL = UNIPROT + '/' + options.accession + '.fasta'
        if options.output:
            ouF = options.output
        else:
            ouF = options.accession + '.fasta'
        if os.path.exists(ouF):
            print('Warning: %s exists' % ouF)

        inFile = urllib.urlopen(URL)
        ouFile = open(ouF, 'w')

        D = {}
        L = []
        for line in inFile:
            line = line.strip()
            if len(line) > 0:
                if line[0] == '>':
                    head = line
                    D.setdefault(head, [])
                    L.append(head)
                else:
                    D[head].append(line)

        for k in D:
            D[k] = ''.join(D[k])

        for k in L:
            head = k
            seq = D[k]
            L = len(seq)
            if L < options.length:
                print('Warning: length of the following protein is \
less than the shortest sequence length')
                print(head)
            for i in range(L, options.length - 1, -1):
                s = seq[0:i]
                fields = head.split()
                fs = fields[0].split('|')
                hd = '%s|%s-%s-%s|%s-%s-%s %s' % \
                     (fs[0], fs[1], 1, i, fs[2],
                      1, i, ' '.join(fields[1:]))
                ouFile.write(hd + '\n')
                ouFile.write(s + '\n')
            for i in range(1, L - options.length + 1, 1):
                s = seq[i:L]
                fields = head.split()
                fs = fields[0].split('|')
                #hd = '|'.join([fs[0], fs[1] + '-' + str(i+1) + '-'
                #              + str(L), fs[2] + '-' + str(i+1) + '-'
                #              + str(L)]) + ' ' + ' '.join(fields[1:])
                hd = '%s|%s-%s-%s|%s-%s-%s %s' % \
                     (fs[0], fs[1], i+1, L, fs[2],
                      i+1, L, ' '.join(fields[1:]))
                ouFile.write(hd + '\n')
                ouFile.write(s+'\n')
        inFile.close()
        ouFile.close()
    elif options.file:
        inF = options.file
        if options.output:
            ouF = options.output
        else:
            ouF = options.file + '.fasta'
        if not os.path.exists(inF):
            print('Warning: input file %s does not exist' % inF)
        if os.path.exists(ouF):
            print('Warning: %s exists' % ouF)

        inFile = open(inF)
        ouFile = open(ouF, 'w')

        D = {}
        L = []
        for line in inFile:
            line = line.strip()
            if len(line) > 0:
                if line[0] == '>':
                    head = line
                    D.setdefault(head, [])
                    L.append(head)
                else:
                    D[head].append(line)

        for k in D:
            D[k] = ''.join(D[k])

        for k in L:
            head = k
            seq = D[k]
            L = len(seq)
            if L < options.length:
                print('Warning: length of the protein is \
less than the shortest sequence length')
                print(head)
            for i in range(L, options.length - 1, -1):
                s = seq[0:i]
                if headFormat(head) == 1:
                    fields = head.split()
                    fs = fields[0].split('|')
                    hd = '%s|%s-%s-%s|%s-%s-%s %s' % \
                         (fs[0], fs[1], 1, i, fs[2],
                          1, i, ' '.join(fields[1:]))
                    ouFile.write(hd + '\n')
                    ouFile.write(s + '\n')
                else:
                    AC = 'AC'
                    ID = 'ID'
                    hd = '>IS|%s_%s-%s-%s|%s_%s-%s-%s %s' \
                         % (AC, get_time(), 1, i, ID,
                            get_time(), 1, i, head[1:])

                    ouFile.write(hd + '\n')
                    ouFile.write(s + '\n')
            for i in range(1, L - options.length + 1, 1):
                s = seq[i:L]
                if headFormat(head) == 1:
                    fields = head.split()
                    fs = fields[0].split('|')
                    hd = '%s|%s-%s-%s|%s-%s-%s %s' % \
                         (fs[0], fs[1], i+1, L, fs[2],
                          i+1, L, ' '.join(fields[1:]))
                    ouFile.write(hd + '\n')
                    ouFile.write(s+'\n')
                else:
                    hd = '>IS|%s_%s-%s-%s|%s_%s-%s-%s %s' \
                         % (AC, get_time(), i+1, L, ID,
                            get_time(), i+1, L, head[1:])
                    ouFile.write(hd + '\n')
                    ouFile.write(s+'\n')
        inFile.close()
        ouFile.close()

    elif options.sequence:
        if options.output:
            ouF = options.output
        else:
            print('Warning: must specify the output \
                  file when using -s option')
            exit()
        if os.path.exists(ouF):
            print('Warning: %s exists' % ouF)
        ouFile = open(ouF, 'w')

        head = options.sequence
        seq = options.sequence
        L = len(seq)
        if L < options.length:
            print('Warning: length of the protein is \
less than the shortest sequence length')
            print(seq)

        for i in range(L, options.length-1, -1):
            s = seq[0:i]
            AC = 'AC'
            ID = 'ID'
            hd = '>IS|%s_%s-%s-%s|%s_%s-%s-%s insillico truncated protein' \
                 % (AC, get_time(), 1, i, ID, get_time(), 1, i)
            #info = ['C', str(L), str(1), str(i)]
            ouFile.write(hd + '\n')
            ouFile.write(s + '\n')
        for i in range(1, L - options.length + 1, 1):
            s = seq[i:L]
            hd = '>IS|%s_%s-%s-%s|%s_%s-%s-%s insillico truncated protein' \
                 % (AC, get_time(), i+1, L, ID, get_time(), i+1, L)
            #info = ['N', str(L), str(i+1), str(L)]
            ouFile.write(hd + '\n')
            ouFile.write(s+'\n')
        ouFile.close()

    else:
        print('Specify one option among "-a, -f and -s" \
or use "-h" to see the help information.')
        exit()


def headFormat(head):
    rsp = 0
    if head[0] == '>':
        fields = head.split()
        fs = fields[0].split('|')
        if len(fs) == 3:
            rsp = 1
    return rsp


def get_time():
    #get_time() = '_'.join([str(x) for x in time.localtime()[0:6]])
    TIME = time.time()
    return TIME


if __name__ == '__main__':
    main()
