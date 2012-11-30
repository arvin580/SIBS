#!/bin/env python
import sys
from optparse import OptionParser
from StructuralVariation import StructuralVariation

parser = OptionParser()
parser.add_option('-f', '--file', dest = 'bam', help = 'input bam or sam file')
parser.add_option('-r', '--refernce', dest = 'ref', help = 'reference genome, such as hg19')
parser.add_option('-b', '--bowtie', dest = 'bowtie_index', help = 'the bowtie indexed reference')
(options, args) = parser.parse_args()

sv = StructuralVariation(options.bam, options.ref, options.bowtie_index)
