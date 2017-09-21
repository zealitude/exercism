<?php

//
// This is only a SKELETON file for the "Hamming" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

function distance($a, $b)
{
    //
    // YOUR CODE GOES HERE
    //
    
    $len = count(str_split($a));
    if(count(str_split($b))!==$len){
        throw new InvalidArgumentException('DNA strands must be of equal length.');
    }

    $distance = 0;
    for ($i=0; $i < $len ; $i++) { 
        if($a[$i] !== $b[$i]){
            $distance++;
        } 
    }

    return $distance;
}
