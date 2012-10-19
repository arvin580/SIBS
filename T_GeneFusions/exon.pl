open INFILE,"<exon";
open OUTFILE,">exon_out";
my $title="";
my $seq="";
my $num=0;
while(<INFILE>)
{
	if(/^>/)
	{
		$fileArray[$num][0]=$title;
		$fileArray[$num][1]=$seq;
		chomp($_);
		$title=$_;
		$seq="";
		$num++;
	}
	else
	{
		chomp($_);
		$seq.=$_;
	}
}
$fileArray[$num][0]=$title;
$fileArray[$num][1]=$seq;
for($i=1;$i<=$num;$i++)
{
	printf OUTFILE "$fileArray[$i][0]\n";
	printf OUTFILE "$fileArray[$i][1]\n";
}

