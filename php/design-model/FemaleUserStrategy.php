<?php

namespace shejimoshi;

class FemaleUserStrategy implements UserStrategy
{
    function showAd()
    {
        echo '2015女装';
    }

    function showCategory()
    {
        echo '女装';
    }
}