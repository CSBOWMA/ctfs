<?php

function xor_encrypt($in) {
    $key = 'eDWo';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}


$data = '{"showpassword":"yes","bgcolor":"#ffffff"}';

$encodedData = base64_encode(xor_encrypt($data));

echo $encodedData

?>
