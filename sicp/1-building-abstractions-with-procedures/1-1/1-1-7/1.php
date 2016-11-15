<?php

echo self_sqrt(3);

function self_sqrt($x) {
    return sqrt_iter(1.0, $x);
}

function sqrt_iter($guess, $x) {
    if (good_enough($guess, $x)) {
        return $guess;
    } else {
        return sqrt_iter(improve($guess, $x), $x);
    }
}

function improve($guess, $x) {
    return ($guess + ($x / $guess)) / 2;
}

function good_enough($guess, $x) {
    return self_abs($guess*$guess - $x) < 0.001;
}

function self_abs($x) {
    if ($x < 0) return -$x; return $x;
}