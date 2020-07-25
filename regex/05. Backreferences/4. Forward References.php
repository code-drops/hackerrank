'''
You have a test string S.
Your task is to write a regex which will match S, with following condition(s):

S consists of tic or tac.
tic should not be immediate neighbour of itself.
The first tic must occur only when tac has appeared at least twice before.
'''

$Regex_Pattern = '/^(\\2tic|(tac))+$/'; //Do not delete '/'. Replace __________ with your regex.

<?php

$Regex_Pattern = '/^(\\2tic|(tac))+$/';
$handle = fopen ("php://stdin","r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)){
    print ("true");
} else {
    print ("false");
}

fclose($handle);
?>
