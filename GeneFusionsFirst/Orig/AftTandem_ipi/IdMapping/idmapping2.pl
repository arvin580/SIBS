open INFILE,"groupid_mapping";
open OUTFILE,">groupid_mapped";
while(<INFILE>)
{
	chomp;
	s/\r$//g;
	if(/dta/)
	{
		@a=split(/\t/,$_);
		$hash{$a[1]}=$a[0];

	}
}
open INFILEa,"fusion_point_hits_1_lung";
while(<INFILEa>)
{
	chomp;
	s/\r$//g;
	if(/xml/)
	{
		/output_(.*)\.2011.*\_(\w+)/;
		$x=$1;
		$y=$2;
		$x=~s/\_/\//;
		$x=~s/\_/\//;
		#print "$x\t$y\n";
		keys %hash;
		while(($key,$val)=each %hash)
		{
			if($key=~/$x/ && $val==$y)
			{
				printf OUTFILE "$_\t$key\n";
			}
		}

	}
	else
	{
		printf OUTFILE "$_\n";
	}
}
