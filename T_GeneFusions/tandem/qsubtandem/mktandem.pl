open INFILE,"<filename";
open OUTFILEa,">../qsubtandem.sh";
while(<INFILE>)
{
chomp;
s/\r$//g;
$filename=$_;
$filename=~s/^inputxml\///g;
$filename=~s/.xml$//g;
printf OUTFILEa "qsub qsubtandem/$filename.sh\n";
open OUTFILE,">$filename.sh";
printf OUTFILE "#!/bin/bash\n";
printf OUTFILE "### Job name\n";
printf OUTFILE "#LJRS -N tandem$num\n";
printf OUTFILE "### Queue name\n";
printf OUTFILE "#LJRS -q dpool\n";
printf OUTFILE "### Number of nodes\n";
printf OUTFILE "#LJRS -l nodes=2:ppn=4\n\n";
printf OUTFILE "cd /netshare1/home1/people/hansun/GeneFusions/Tandem\n\n";
printf OUTFILE "tandem.exe $_\n";
close OUTFILE;
}
close OUTFILEa;
