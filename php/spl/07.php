<?php

$file = new SplFileInfo('cs.txt');

echo 'ctime:'.date('Y-m-d H:i:s', $file->getCTime())."\n";

//读取文件内容
$fileObj = $file->openFile('r');

while($fileObj->valid()) {
    echo $fileObj->fgets();
}

$fileObj = null;//关闭资源
$file = null;