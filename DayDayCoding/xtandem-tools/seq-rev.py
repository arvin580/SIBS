#!/usr/bin/env python
import sys
import string
trans = string.maketrans('ATCGatcg','TAGCtagc')
seq = sys.argv[1]
seq_rev = seq[::-1]
print(string.translate(seq_rev,trans))

