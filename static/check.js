function getBrowserVersion() {
    var userAgent = navigator.userAgent;
    var version;
    
    // Check for Chrome
    if (/chrome/i.test(userAgent)) {
      version = userAgent.match(/chrome\/(\d+)/i)[1];
    }
    // Check for Firefox
    else if (/firefox/i.test(userAgent)) {
      version = userAgent.match(/firefox\/(\d+)/i)[1];
    }
    // Check for Safari
    else if (/safari/i.test(userAgent)) {
      version = userAgent.match(/version\/(\d+)/i)[1];
    }
    
    return parseInt(version);
  }
  
  function checkBrowserVersion() {
    var chromeThreshold = 73;
    var firefoxThreshold = 68;
    var safariThreshold = 14;
    
    var currentVersion = getBrowserVersion();
    
    if (/chrome/i.test(navigator.userAgent) && currentVersion < chromeThreshold) {
      alert("Please download the latest version of Chrome.");
    }
    else if (/firefox/i.test(navigator.userAgent) && currentVersion < firefoxThreshold) {
      alert("Please download the latest version of Firefox.");
    }
    else if (/safari/i.test(navigator.userAgent) && currentVersion < safariThreshold) {
      alert("Please download the latest version of Safari.");
    }
  }
  
  checkBrowserVersion();
  