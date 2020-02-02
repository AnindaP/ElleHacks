chrome.runtime.onInstalled.addListener(function(){
    chrome.tabs.create({url: "http://localhost:8080/webapp2/installed.html"}, function (tab) {
        console.log("New tab launched with http://localhost:8080/webapp2/installed.html");
    });
});

chrome.browserAction.onClicked.addListener(function(activeTab){
    var newURL = "http://stackoverflow.com/";
    chrome.tabs.create({ url: newURL });
});
