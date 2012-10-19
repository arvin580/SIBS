open INFILE,"<exon_fusion";
open OUTFILE,">exon_fusion_validate";
$gene12="$ARGV[0]:$ARGV[1]";
$gene21="$ARGV[1]:$ARGV[0]";

while($f=<INFILE>)
{
	$s=<INFILE>;
	chomp($f);
	chomp($s);
	if($f=~/$gene12/||$f=~/$gene21/)
	{
		printf OUTFILE "$f\n";
		printf OUTFILE "$s\n";
	}
}
close(INFILE);
close(OUTFILE);
