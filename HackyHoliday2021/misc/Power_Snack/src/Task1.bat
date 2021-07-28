for ($i = 1 ; $i -lt 1338 ; $i++) {

   if($i % 42  -eq 0) {
       
       Write-Output 'Life, the universe, and everything'
       
   } else {
   
       Write-Output $i
   
   }
}