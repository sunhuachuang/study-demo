<?php

namespace shejimoshi;

class MaleUserStrategy implements UserStrategy
{
    public function showAd()
    {
        echo '2015款男装';
    }

    public function showCategory()
    {
        echo '男装';
    }
}