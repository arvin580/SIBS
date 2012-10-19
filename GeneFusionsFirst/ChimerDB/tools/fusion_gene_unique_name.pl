open INFILE,"<fusion_gene_unique";
open OUTFILE,">fusion_gene_unique_name";
while(<INFILE>)
{
	chomp;
	s/\r$//g;
	@arr=split(/\t+/,$_);
	printf OUTFILE "$arr[0]\n";
	printf OUTFILE "$arr[1]\n";
}
