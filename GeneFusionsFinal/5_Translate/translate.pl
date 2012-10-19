### perl translate.pl exon_fusion exon_fusion_peptide 
### perl translate.pl splicing_exon  splicing_exon_peptide

open INFILE,"<CodonUsage";
open INFILE1,"<$ARGV[0]";
open OUTFILE,">$ARGV[1]";
my %codon;
while(<INFILE>)
{
        chomp;
        s/\r$//g;
	@a=split(/\s+/);
	$codon{$a[0]}=$a[1];

}
while($t=<INFILE1>)
{
	$c=<INFILE1>;
	chomp($t);
        $t=~s/\r$//g;
	chomp($c);
        $c=~s/\r$//g;
	$codon=undef;
	$peptide=undef;
	@a=split(/:/,$t);
	$juction=$a[5];
	$juctionsecond=$a[6];
	$loci=undef;
	$int=undef;
	$intsecond=undef;
	for($i=0;$i<=length($c)-3;$i=$i+3)
	{
		$three=substr($c,$i,3);
		if(exists($codon{$three}))
		{
			$peptide.=$codon{$three};
		}
		else
		{
			$peptide.="?";
		}
		
	}
	        if($juction % 3==0)
		{
			$int=int($juction/3);
			$intsecond=int($juctionsecond/3);
			$loci="$int|0|$intsecond";

		}
		elsif($juction %3 ==1)
		{
                        $int=int($juction/3)+1;
			$intsecond=int(($juctionsecond-2)/3);
			$loci="$int|-2|$intsecond";


		}
		elsif($juction %3 ==2)
		{
                        $int=int($juction/3)+1;
			$intsecond=int(($juctionsecond-1)/3);
			$loci="$int|-1|$intsecond";


		}

	        

		printf OUTFILE "$t|0|$loci|\n";
		printf OUTFILE "$peptide\n";

	$peptide=undef;
	for($i=1;$i<=length($c)-3;$i=$i+3)
	{
                $three=substr($c,$i,3);
		if(exists($codon{$three}))
		{
			$peptide.=$codon{$three};
		}
		else
		{
			$peptide.="?";
		}
	
	}
                if(($juction-1) % 3==0)
		{
			$int=int(($juction-1)/3);
			$intsecond=int($juctionsecond/3);
			$loci="$int|0|$intsecond";

		}
		elsif(($juction-1) %3 ==1)
		{
                        $int=int(($juction-1)/3)+1;
			$intsecond=int(($juctionsecond-2)/3);
			$loci="$int|-2|$intsecond";


		}
		elsif(($juction-1) %3 ==2)
		{
                        $int=int(($juction-1)/3)+1;
			$intsecond=int(($juctionsecond-1)/3);
			$loci="$int|-1|$intsecond";


		}

         	printf OUTFILE "$t|1|$loci|\n";
		printf OUTFILE "$peptide\n";

	$peptide=undef;
	for($i=2;$i<=length($c)-3;$i=$i+3)
	{
                $three=substr($c,$i,3);
		if(exists($codon{$three}))
		{
			$peptide.=$codon{$three};
		}
		else
		{
			$peptide.="?";
		}
	
	}
                if(($juction-2) % 3==0)
		{
			$int=int(($juction-2)/3);
			$intsecond=int($juctionsecond/3);
			$loci="$int|0|$intsecond";

		}
		elsif(($juction-2) %3 ==1)
		{
                        $int=int(($juction-2)/3)+1;
			$intsecond=int(($juctionsecond-2)/3);
			$loci="$int|-2|$intsecond";


		}
		elsif(($juction-2) %3 ==2)
		{
                        $int=int(($juction-2)/3)+1;
			$intsecond=int(($juctionsecond-1)/3);
			$loci="$int|-1|$intsecond";


		}
        	printf OUTFILE "$t|2|$loci|\n";
                $peptide=~s/\?$//;
		printf OUTFILE "$peptide\n";


}
close(INFILE);
close(INFILE1);
close(OUTFILE);
