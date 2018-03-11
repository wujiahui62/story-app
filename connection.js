var page = require('webpage').create()
page.open(url, function(status) {
    if(status != "success") {
        console.log('Fail to load the address');
    } else {
       var title = page.evaluate(function() {
           return document.title;
       });
       console.log('Page title is ' + title);
       phantom.exit();
    }
});