open INFILE,"<splicing_exon_peptide";
open OUTFILE,">splicing_exon_peptide_qc";
open OUTFILEa,">splicing_exon_peptide_qc_gap";
while($title=<INFILE>)
{
$seq=<INFILE>;
@arr=split(/\|/,$title);
$point=$arr[2];
if((index($seq,"*")>=$point)||(index($seq,"*")==-1))
{
printf OUTFILE "$title";
printf OUTFILE "$seq";
}
else
{
printf OUTFILEa "$title";
printf OUTFILEa "$seq";
}


}
