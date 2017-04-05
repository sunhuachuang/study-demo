var page = require('webpage').create();
page.open('http://lovesun.xyz', function () {
    page.render('lovesun.png');
    phantom.exit();
});
