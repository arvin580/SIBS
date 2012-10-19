open INFILE,"<fusion_point_3_2hit_groupid";
$num=0;

while(<INFILE>)
{
	chomp;
	s/\r$//;
	$adc=0;
	$scc=0;
	$normal=0;

	@arr=split(/\t+/,$_);
	for($i=2;$i<@arr;$i++)
	{
		if($arr[$i]=~/ADC/)
		{
			$adc++;
		}
		if($arr[$i]=~/SCC/)
		{
			$scc++;
		}
		if($arr[$i]=~/Normal/)
		{
			$normal++;
		}
		$file[$num][0]=$adc;
		$file[$num][1]=$scc;
		$file[$num][2]=$normal;
	}
	$num++;
}
for($i=0;$i<$num;$i++)
{
	print "$file[$i][0]\t$file[$i][1]\t$file[$i][2]\n";

}
