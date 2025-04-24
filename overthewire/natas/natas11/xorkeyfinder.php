<?php

function xor_encrypt($in) {
    $key = '{"showpassword":"no","bgcolor":"#ffffff"}';
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}


$data = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg%3D";

$decodedData = xor_encrypt(base64_decode($data));

echo $decodedData

?>
