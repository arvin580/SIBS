#!/usr/bin/perl
open INFILE,"<$ARGV[0]";
open OUTFILE,">$ARGV[1]";
open OUTFILEx,">$ARGV[2]";
my $pre;
my @arr;
for(my $i=0;$i<3;$i++)
{
$pre=<INFILE>;
printf OUTFILE $pre;
printf OUTFILEx $pre;
}
while(<INFILE>)
{
	@arr=split(/\t+/,$_);
	if($arr[1]==77||$arr[1]==141||abs($arr[8])>225||abs($arr[8])<175)
	{
         printf OUTFILEx $_;
	}

	#if($arr[1]==77||$arr[1]==141)
        # {
        # }
	else
	{
        printf OUTFILE $_;
	}
}
close(INFILE);
close(OUTFILE);
close(OUTFILEx);
