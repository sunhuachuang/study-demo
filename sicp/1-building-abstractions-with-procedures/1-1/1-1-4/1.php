<?php

function square($x)
{
    return $x * $x;
}

echo square(5);

function sum_of_square($x, $y)
{
    return square($x) + square($y);
}

echo sum_of_square(2, 3);

$a = function($x) { return $x * $x; };

echo $a(5); //25