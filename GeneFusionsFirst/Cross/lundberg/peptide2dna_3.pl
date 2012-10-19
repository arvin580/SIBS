open INFILE,"peptide_complete_c_title";
open OUTFILE,">peptide_complete_c_title_dna";
while($peptide=<INFILE>)
{
$title=<INFILE>;
chomp($title);
$title=~s/\r$//g;
open INFILEa,"../Translate/exon_fusion";
while($s1=<INFILEa>)
{
$s2=<INFILEa>;
if($s1=~/$title/)
{
printf OUTFILE "$peptide";
printf OUTFILE "$s1";
printf OUTFILE "$s2";
}
}
close(INFILEa)
}
