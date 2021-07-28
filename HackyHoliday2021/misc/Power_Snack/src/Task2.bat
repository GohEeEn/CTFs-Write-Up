# Sort by line length
Get-Content ./dictionary | sort { $_.length }

# Select string that matches this regex / contains only these characters "iydhlao" for 2 letters or more
select-string -pattern "^[IYDHLAO][iydhlao]+$"




# alternative
ForEach ($word in $_) { if($word.ToCharArray() | Group | Select Count | Where -Property Count -eq 1) Write-Output $word }

$W | select-string -pattern "^[IYDHLAO][iydhlao]+$" -CaseSensitive