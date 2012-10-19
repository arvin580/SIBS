open INFILE,"<$ARGV[0]";
open OUTFILE,">$ARGV[1]";
my %hash;
my @arr;
<INFILE>;
<INFILE>;
<INFILE>;
while(<INFILE>)
{
	#@arr=split(/\s+/,$_);
	/\s+(\d+)\s+/;
	if(!exists($hash{$1}))
	{
		$hash{$1}=$1;
	}
	
}
while(($key,$val)=each %hash)
{
	printf OUTFILE "$key\n";
}
