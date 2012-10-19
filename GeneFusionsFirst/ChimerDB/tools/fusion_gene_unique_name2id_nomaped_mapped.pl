open INFILE,"<fusion_gene_unique_name2id_nomaped_mapped";
open OUTFILE,">fusion_gene_unique_name2id_nomaped_mapped_checked";
while(<INFILE>)
{
	chomp;
	s/\r$//g;
	@arr=split(/\t/,$_);
	$first=$arr[0];
	$second=$arr[1];
	@fi=split(/\|/,$first);
	@se=split(/\|/,$second);
	for($i=0;$i<@fi;$i++)
	{
		for($j=0;$j<@se;$j++)
		{
			printf OUTFILE "$fi[$i]\t$se[$j]\n";
		}
	}

}
