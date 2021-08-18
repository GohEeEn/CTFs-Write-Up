$answer = 

# Get every word from the dictionary file that
# got sorted by length, then by ordering
ForEach($word In $(Get-Content ./dictionary | Sort-Object {$_.Length}, {$_.ToString()})) {
	
	# 1st requirement : only words longer than 1 character
	if($word.Length -gt 1) {
		$letters = "iydhlao"
		$match = 1

		# 2nd requirement : eliminate the dict word that contains letter other than those given
		ForEach($char in $word.ToCharArray()) {
			if(!($letters.Contains($char))) {
				$match = 0
			}
			$letters = $letters -replace $char,""
		}

		if($match) {
			Write-Output([string]$word)
		}
	}
}


$answer | check