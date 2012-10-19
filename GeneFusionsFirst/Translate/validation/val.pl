open INFILE,"../exon_fusion_peptide";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($title=~/COL1A1/ && $title=~/COL1A2/)
{
print $title;
print $seq;
}

}
