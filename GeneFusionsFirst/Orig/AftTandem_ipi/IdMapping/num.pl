open INFILE,"fusion_point_hits_1_lung";
while(<INFILE>)
{
	if(/^(\d+)/)
	{
		$num++;
		$x=$1;
		if($x>1)
		{
			$num2++;
		}
		elsif($x==1)
		{
			$num1++;
		}
	}
}
print "$num\n$num2\n$num1\n";
