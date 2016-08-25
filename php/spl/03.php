<?php

class OuterImpl extends IteratorIterator
{
    public function current()
    {
        return parent::current()."_tail";
    }

    public function key()
    {
        return "Pre_".parent::key();
    }
}

$array = array('a', 'b', 'c','d');
$outerObj = new OuterImpl(new ArrayIterator($array));

foreach ($outerObj as $key => $value) {
    echo $key.'--'.$value."\n";
}