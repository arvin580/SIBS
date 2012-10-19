# perl position_cmp.pl gene.position SV_lung_Nature_Lee
open INFILE,"$ARGV[0]";
open OUTFILE,">$ARGV[0].$ARGV[1]";
while($x=<INFILE>)
{
	chomp($x);
	$x=~s/\r$//g;
	@a=split(/\t/,$x);
        open INFILEa,"$ARGV[1]";
	while($y=<INFILEa>)
	{
		chomp($y);
		$y=~s/\r$//g;
		@b=split(/\t/,$y);
	#	if(($a[1] eq $b[1]) && ($a[4] eq $b[4]))
		if(($a[1] eq $b[2]))
		{
			if($b[4]<$a[2]-5000 || $b[3]>$a[3]+5000)
			{
			}
			else
			{
				printf OUTFILE "$x\t$y\n";
			}
		}
	}
	close(INFILEa);
}
close(INFILE);
