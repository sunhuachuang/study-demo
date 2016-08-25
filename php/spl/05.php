<?php
/*
function __autoload($className)
{
    require_once('load/'.$className.'.php');
}
*/

function loadClass($className)
{
    require_once('load/'.$className.'.php');
}

spl_autoload_register('loadClass');

new Test();