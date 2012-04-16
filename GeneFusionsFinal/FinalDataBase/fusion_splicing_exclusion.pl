open INFILE,"$ARGV[0]";
while(<INFILE>)
{
chomp;
$hash{$_}++;
}


open INFILEa,"fusion_splicing_uniprot_ensembl_contaminated_final";
open OUTFILE,">$ARGV[1]";

while($t=<INFILEa>)
{
$s=<INFILEa>;
$flag=0;
while(($key,$val)=each %hash)
{
if($s=~/$key/)
{
$flag=1;
}
}
if($flag==0)
{
printf OUTFILE "$t";
printf OUTFILE "$s";
}
}
close(INFILE);
close(OUTFILE);
close(OUTFILEa);
