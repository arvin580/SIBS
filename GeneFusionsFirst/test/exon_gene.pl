open INFILE,"<../Ensemble/exon_line";
open INFILE1,"<fusion_gene_unique";
open OUTFILE1,">exon_id";
open OUTFILE2,">exon_name";
open OUTFILE3,">exon_fusion";
open OUTFILE4,">fusion_gene_unique_unmapped";
my %gene_id_hash;
my %gene_name_hash;
while(<INFILE>)
{
	chomp($_);
        s/\r$//g;
	if(/^>/)
	{
		@a=split(/\|/,$_);
	}
	else
	{
			$gene_id_hash{$a[0]}.="$_&";
			$gene_name_hash{">$a[5]"}.="$_&";
	}

}
keys %gene_id_hash;
while(($key,$val)=each(%gene_id_hash))
{
	printf OUTFILE1 "$key\n";
	printf OUTFILE1 "$val\n";
}

keys %gene_name_hash;
while(($key,$val)=each(%gene_name_hash))
{
	printf OUTFILE2 "$key\n";
	printf OUTFILE2 "$val\n";
}

while(<INFILE1>)
{
	chomp;
	@gene=split(/\s+/,$_);

if(exists($gene_name_hash{">$gene[0]"})&& exists($gene_name_hash{">$gene[1]"}))
{
	@first=split(/&/,$gene_name_hash{">$gene[0]"});
	@second=split(/&/,$gene_name_hash{">$gene[1]"});
	$fi=@first;
	$se=@second;
	for($i=0;$i<$fi;$i++)
	{
		for($j=0;$j<$se;$j++)
		{
			$lf=length($first[$i]);
			$ls=length($second[$j]);
			printf OUTFILE3 ">genefusions:$gene[0]:$gene[1]:$i:$j:$lf:$ls\n";
			$fusion=$first[$i].$second[$j];
			printf OUTFILE3 "$fusion\n";
                        
			printf OUTFILE3 ">genefusions:$gene[1]:$gene[0]:$j:$i:$ls:$lf\n";
			$fusion=$second[$j].$first[$i];
			printf OUTFILE3 "$fusion\n";
		}
	}
       
}
else
{
	printf OUTFILE4 "$gene[0]\t$gene[1]\n";
}
}

close(INFILE);
close(INFILE1);
close(OUTFILE1);
close(OUTFILE2);
close(OUTFILE3);
close(OUTFILE4);
