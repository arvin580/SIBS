open INFILE,"<fusion_gene";
open OUTFILE,">fusion_gene_unique";
my %fusion_gene;
while(<INFILE>)
{
	chomp($_);
	@a=split(/\t/,$_);
	$fs="$a[0]\t$a[1]";
	$sf="$a[1]\t$a[0]";
	if(exists($fusion_gene{$fs})||exists($fusion_gene{$sf}))
	{
		if(exists($fusion_gene{$fs}))
		{
			$fusion_gene{$fs}++;

		}
		if(exists($fusion_gene{$sf}))
		{
			$fusion_gene{$sf}++;
		}


	}
	else
	{
		$fusion_gene{$fs}=1;

	}
}
keys %fusion_gene;
while(($key,$val)=each(%fusion_gene))
{
	#printf OUTFILE "$key\t$val\n";
	printf OUTFILE "$key\n";
}
