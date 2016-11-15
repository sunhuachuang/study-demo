<?php
function fib_recursive($n)
{
    if ($n === 0 || $n === 1) {
        return $n;
    }
    return fib_recursive($n-1) + fib_recursive($n - 2);
}

echo fib_recursive(6), "\n";

function fib_itertion($n)
{
    function fib_iter($a, $b, $count)
    {
        if ($count === 0) {
            return $b;
        }
        return fib_iter($a + $b, $a, $count - 1);
    }

    return fib_iter(1, 0, $n);
}

echo fib_itertion(6), "\n";
