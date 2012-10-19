open INFILE,"<fusion_gene_unique";
open INFILEa,"<fusion_gene_unique_adding";
open OUTFILE,">fusion_gene_unique_final";
while(<INFILE>)
{
chomp;
s/\r$//g;
@arr=split(/\t+/,$_);
$hash{"$arr[0]\t$arr[1]"}++;
}
