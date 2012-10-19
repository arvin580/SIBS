open INFILE,"<uniprot_sprot.fasta_comb_reverse";
open INFILEa,"<uniprot_trembl.fasta_comb_reverse";
open OUTFILE,">uniprot_comb_reverse_human";
while($title=<INFILE>)
{
$seq=<INFILE>;
if($title=~/OS\=Homo sapiens/)
{
printf OUTFILE $title;
printf  OUTFILE $seq;
}
}
while($title=<INFILEa>)
{
$seq=<INFILEa>;
if($title=~/OS\=Homo sapiens/)
{
printf OUTFILE $title;
printf  OUTFILE $seq;
}
}
