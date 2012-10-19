open INFILE,"Ensemble_Protein_Homo_sapiens.GRCh37.61.pep.all.fasta";
open OUTFILE,">ensemble_protein";
$title=undef;
$seq=undef;
$num=undef;;
while(<INFILE>)
{
chomp;
s/\r$//g;
if(/^>/)
{
$num++;
if($num!=1)
{
printf OUTFILE "$title\n";
printf OUTFILE "$seq\n";
$title=undef;
$seq=undef;
}
$title=$_;
}
else
{
$seq.=$_;
}
}
printf OUTFILE "$title\n";
printf OUTFILE "$seq\n";

