<?php

/**
 * auto-loading class use spl_autoload_register()
 * 不使用魔术方法 __autoload(), 因其全局只能有一个，外接lib时会有问题。
 */

function myAutoload($className)
{
    include_once('./'.$className.'.php');
}

spl_autoload_register('myAutoload');

$class = new ClassTest();
$class->render();