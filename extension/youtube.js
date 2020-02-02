const api = "https://www.googleapis.com/youtube/v3";

const apiKey = "AIzaSyD6UPmGAAnGUWra-ESWfg6dq3hWoRA0kQ4";

const videoID = "";

const get = () => fetch(api + "/commentThreads?part=snippet&textFormat=plainText&key=" + apiKey + "&text&videoId=" + videoID + "&maxResults=100")
.then((response) => response.json())