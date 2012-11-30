import sys
from optparse import OptionParser
from StructuralVariation import StructuralVariation

parser = OptionParser()
parser.add_option('-f', '--file', dest = 'bamFile', help = 'input bam file')
(options, args) = parser.parse_args()

sv = StructuralVariation(options.bamFile)
