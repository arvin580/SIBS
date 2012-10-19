open INFILE,"exon_fusion_peptide_interception_qc_comb_reverse";
while(<INFILE>)
{
if(/COL1A1\:EMILIN1\:4\:7\:54\:117\|0\|18\|0\|39\|\|18\|30/)
{
print;
$a=<INFILE>;
print $a;
}
}
