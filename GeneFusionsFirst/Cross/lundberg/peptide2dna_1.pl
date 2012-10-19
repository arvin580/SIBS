open INFILE,"peptide";
open OUTFILE,">peptide_complete";
while($peptide=<INFILE>)
{
printf OUTFILE "#$peptide";
chomp($peptide);
$peptide=~s/\r$//g;
open INFILEa,"../FinalDataBase/interception_ipi_reverse_final";
while($title=<INFILEa>)
{
$seq=<INFILEa>;
if($seq=~/$peptide/)
{
printf OUTFILE $title;
printf OUTFILE $seq;
}
}
}
