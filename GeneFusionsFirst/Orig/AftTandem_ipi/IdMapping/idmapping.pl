opendir DIR,"$ARGV[0]";
open OUTFILE,">$ARGV[1]";
foreach $file(readdir DIR)
{
open INFILE,"$ARGV[0]/$file";
while(<INFILE>)
{
	if(/group id="(\w+)"/)
	{
		$id=$1;
	}
	if(/<note label="Description">(.*)<\/note>/)
	{
		$spec=$1;
		chomp($spec);
		$spec=~s/\r//g;
		printf OUTFILE "$id\t$spec\n";
		$id=undef;
		$spec=undef;
	}
}
close(INFILE);
}
closedir DIR;
