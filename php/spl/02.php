<?php
class CountMe implements Countable
{
    protected $myCount =3;
    public function count()
    {
        return $this->myCount;
    }
}

$obj = new CountMe();
echo count($obj);

?>