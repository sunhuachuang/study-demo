<?php
namespace shejimoshi;

function __autoload($className)
{
    require_once($className.'.php');
}

class Page
{
    protected $strategy;

    function index()
    {
        $this->strategy->showAd();
        echo "\n";
        $this->strategy->showCategory();
    }

    function setStrategy(UserStrateg $strategy)
    {
        $this->strategy = $strategy;
    }
}
echo 'a';
$page = new Page;
$stragegy = new FemaleUserStrategy();
$page->setStrategy($stragegy);
$page->index();