<?php

function loadClass($className)
{
    set_include_path("load/");
    echo $className;
    spl_autoload($className);
}

spl_autoload_register('loadClass');

new Test;