<?php

function factorial($n) {
    if ($n === 1) {
        return 1;
    } else {
        return $n * factorial($n - 1);
    }
}

echo factorial(5),"\n";

function factorial2($n) {
    return factIter(1, 1, $n);
}

function factIter($product, $counter, $maxn) {
    if ($counter > $maxn) {
        return $product;
    } else {
        return factIter($product * $counter, $maxn);
    }
}

echo factorial(6),"\n";