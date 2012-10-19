open INFILE,"<../Translate/exon_fusion_peptide";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($title=~/EML4:ALK/ || $title=~/ALK:EML4/)
{
print "$title$seq";
}

}
