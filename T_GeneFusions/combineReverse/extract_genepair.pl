open INFILE,"exon_fusion_peptide_interception_qc_comb_reverse";
while(<INFILE>)
{
if(/COL1A1\:EMILIN1/)
{
print;
$a=<INFILE>;
print $a;
}
if(/EMILIN1\:COL1A1/)
{
print;
$b=<INFILE>;
print $b;
}
}



