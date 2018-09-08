<?php

function from(DateTime $startDateTime){

    $date = new DateTime();
    $date->setTimestamp($startDateTime->getTimestamp());

    // A gigasecond is 10^9 (1,000,000,000) seconds.
    $gigasecond = new DateInterval('PT1000000000S');
    return $date->add($gigasecond);
}