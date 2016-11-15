<?php

$a = -2;
switch ($a) {
case $a == 0:
    echo $a;
case $a > 0:
    echo $a;
case $a < 0:
    echo -$a;
}

function or_abs($x) {
    if ($x == 0 || $x > 0) {
        echo $x;
    } else {
        echo -$x;
    }
}

function and_between($x, $a, $b) {
    if ($x > $a && $x < $b) {
        echo true;
    } elseif ($x != $a || $x != $b) {
        echo false;
    } elseif (!$x == 0) {
        echo $x.'!=0';
    }
}

or_abs(-5);
and_between(2, 3, 4);