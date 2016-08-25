<?php
function chat()
{
    $r = (yield 'yield1');
    var_dump($r);
    $r = (yield 'yield2');
    var_dump($r);
}

$e = chat();
var_dump($e);
var_dump($e->current());
var_dump($e->send('aaa'));
var_dump($e->send('bbb'));

exit;
function logger($fileName)
{
    $f = fopen($fileName, 'a');
    while (true) {
        //var_dump(yield);
        fwrite($f, yield . "\n"); //单纯的接受者
    }
}

$l = logger('../tmp/log');
var_dump($l);

$l->send('aaa');
$l->send('bbb');
$l->send('ccc');
