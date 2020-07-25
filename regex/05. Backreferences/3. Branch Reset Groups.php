'''
You have a test string S.
Your task is to write a regex which will match ,S with following condition(s):
S consists of 8 digits.
S must have "---", "-", "." or ":" separator such that string S gets divided in 4 parts, with each part having exactly two digits.
S string must have exactly one kind of separator.
Separators must have integers on both sides.
'''


<?php

$Regex_Pattern = '/^\d{2}(-(?:--)?|\.|:)\d{2}\1\d{2}\1\d{2}$/'; 
$handle = fopen ("php://stdin","r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)){
    print ("true");
} else {
    print ("false");
}

fclose($handle);
?>
