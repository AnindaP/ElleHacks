function openAlert(){
    chrome.tabs.executeScript({
        file: 'alert.js'
    }); 
}

document.getElementById('fb').addEventListener('click', openAlert);