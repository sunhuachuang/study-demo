<?php
spl_autoload_extensions('.php');
set_include_path(get_include_path().PATH_SEPARATOR.'load/' );
spl_autoload_register();

new Test();
//new Test1();