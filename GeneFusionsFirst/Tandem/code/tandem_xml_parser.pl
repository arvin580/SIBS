### $ARGV[0]:inputdir    $AGV[1]:aft_fdr_dir $ARGV[2]:aft_fdr_fusions_dir
use XML::Parser;
$fdr=0.01;
opendir DIR,"$ARGV[0]";
$parser = XML::Parser->new( Handlers => {Start=>\&handle_start,End=>\&handle_end,});
foreach $filename(readdir DIR)
{
	if($filename=~/xml/)
	{

		%hash=undef;
		$parser->parsefile("$ARGV[0]/$filename");
		$filename=~s/\.xml$//g;
		open OUTFILEa,">$ARGV[1]/$filename\_fdr_validated";
		open OUTFILEb,">$ARGV[2]/$filename\_fdr_validated_fusions";
		keys %hash;
		foreach $key (sort by_score keys %hash)
		{
			$decoy=0;
			$target=0;
			@val=split (/\t/,$hash{$key});
			if($val[2]=~/^REVERSE/)
			{
				$decoy++;
			}
			else
			{
				$target++;
			}
			if(2*$decoy/($decoy+$target)<=$fdr)
			{
				printf OUTFILEa "$hash{$key}\n";
				if(!($val[2]=~/^IPI/))
				{
					printf OUTFILEb "$hash{$key}\n";
				}
			}
			else
			{
				last;
			}
		}

	}
}
sub handle_start {
	my( $expat, $element, %attrs ) = @_;
	if($element eq "group" && $attrs{"type"} eq "model")
	{
		$group_id=$attrs{"id"};
		$group_mh=$attrs{"mh"};
		$group_z=$attrs{"z"};
		$group_rt=$attrs{"rt"};
		$group_expect=$attrs{"expect"};
		$group_label=$attrs{"label"};
		$group_type=$attrs{"type"};
		$group_sumI=$attrs{"sumI"};
		$group_maxI=$attrs{"maxI"};
		$group_fI=$attrs{"fI"};
	}
	if($element eq "protein")
	{
		$protein_expect=$attrs{"expect"};
		$protein_id=$attrs{"id"};
		$protein_uid=$attrs{"uid"};
		$protein_label=$attrs{"label"};
		$protein_sumI=$attrs{"sumI"};
	}
	if($element eq "file")
	{
		$file_type=$attrs{"type"};
		$file_url=$attrs{"URL"};
	}
	if($element eq "peptide")
	{
		$peptide_start=$attrs{"start"};
		$peptide_end=$attrs{"end"};
	}
	if($element eq "domain")
	{
		$domain_id=$attrs{"id"};
		$domain_start=$attrs{"start"};
		$domain_end=$attrs{"end"};
		$domain_expect=$attrs{"expect"};
		$domain_mh=$attrs{"mh"};
		$domain_delta=$attrs{"delta"};
		$domain_hyperscore=$attrs{"hyperscore"};
		$domain_nextscore=$attrs{"nextscore"};
		$domain_y_score=$attrs{"y_socre"};
		$domain_y_ions=$attrs{"y_ions"};
		$domain_b_socre=$attrs{"b_score"};
		$domain_b_ions=$attrs{"b_ions"};
		$domain_pre=$attrs{"pre"};
		$domain_post=$attrs{"post"};
		$domain_seq=$attrs{"seq"};
		$domain_missed_cleavages=$attrs{"missed_cleavages"};
	}
	if($element eq "aa")
	{
		$aa_type=$attrs{"type"};
		$aa_at=$attrs{"at"};
		$aa_modified=$attrs{"modified"};
		$aa="$aa_type:$aa_at:$aa_modified";
		$aas.="$aa|";
		$aas=~s/\|$//g;
	}
}
sub handle_end {
	my( $expat, $element ) = @_;
	if($element eq "protein")
	{
#		print "$group_id\t$group_expect\t$group_label\t$protein_id\t$protein_label\t$protein_expect\t$peptide_start\t$peptide_end\t$domain_id\t$domain_start\t$domain_end\t$domain_hyperscore\t$domain_expect\t$domain_seq\t$domain_pre\t$domain_post\n";
		$hash{"$filename\_$group_id"}="$filename\_$group_id\t$protein_id\t$protein_label\t$protein_expect\t$domain_id\t$domain_start\t$domain_end\t$domain_expect\t$domain_hyperscore\t$domain_seq\t$aas";
		$aas=undef;
	}
}
sub by_score
{
	@a_val=split (/\t/,$hash{$a});
	@b_val=split (/\t/,$hash{$b});
	$b_val[8]<=>$a_val[8];
}
