open INFILE,"<CodonUsage";
open OUTFILE,">exon_fusion_peptide";
open INFILE1,"<exon_fusion";
my %codon;
while(<INFILE>)
{
	@a=split(/\s+/);
	$codon{$a[0]}=$a[1];

}
#keys %codon;
#while(($key,$val)=each(%codon))
#{
#	print "+++$key+++$val+++\n"
#}

while($t=<INFILE1>)
{
	$c=<INFILE1>;
	chomp($t);
	chomp($c);
        $t=~s/\r//;
        $c=~s/\r//;
	$codon=undef;
	$peptide=undef;
	@a=split(/:/,$t);
	$juction=$a[4];
	$juctionsecond=$a[5];
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
                $peptide=~s/\?$//;
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
                $peptide=~s/\?$//;
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
