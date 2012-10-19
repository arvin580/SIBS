$st=time;
open INFILE,"<$ARGV[0]";
open OUTFILE,">$ARGV[1]";
my @arr;
my @siteinfo;
my $flag=0;
my $i;
my $max=3000000;
while(<INFILE>)
{
	/\s+(\d+)\s+\w+\s+(\d+)/;
	$siteinfo[$1]=$2;

}
for($i=1;$i<=$max;$i++)
{
	if($flag==0)
	{
	if($siteinfo[$i]>0)
	{
		$start=$i;
		$flag=1;
	}
        }
	else
	{
		if($siteinfo[$i]==0)
		{
			$end=$i-1;
			printf OUTFILE "$start\t$end\n";
			$flag=0;
		}
	}

}
$t=time-$st;
print "$t\n";
=cut
my @arr;
my $start=0;
my $end=0;
my $flag=0;
while(<INFILE>)
{
	@arr=split(/\s+/,$_);
	if($flag==0)
	{
	if($arr[3]>0)
	{
		$start=$arr[1];
		$flag=1;
	}
        }
	else
	{
        if($arr[3]>0)
	{
		$end=$arr[1];
	}
	else
	{
                printf OUTFILE "$start\t$end\n";
		$flag=0;
	}

	}

}
=cut
