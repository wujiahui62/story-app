var page = require('webpage').create()
page.open("http://chinesestory.pythonanywhere.com", function(status) {
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