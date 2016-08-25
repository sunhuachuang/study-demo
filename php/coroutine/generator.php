<?php
function xrange($start, $end, $step = 1)
{
    for ($i = $start; $i < $end; $i += $step) {
        yield $i;
    }
}

var_dump(xrange(1, 10));
var_dump(xrange(1, 10) instanceof Iterator);

exit;
foreach (xrange(1, 100, 2) as $n) {
    echo $n, "\n";
}