chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    splitUrl = url.split("/")
    var playerId = splitUrl[splitUrl.length-1];

    
    
    var API_URL = 'httpa://osu.ppy.sh/api/v2'
    var TOKEN_URL = 'https://osu.ppy.sh/oauth/token'


    var data = new FormData();
    data.append('client_id', 8161);
    data.append('client_secret', '5oZdzZclpCtmzc8OTiFZZguCcVvoyQfpwiFuAX01');
    data.append('grant_type', 'client_credentials');
    data.append('scope', 'public');
    var requests = new XMLHttpRequest();
    requests.open('POST', TOKEN_URL, true)

    requests.send(data)

    function extend(dest, src) { 
        for(var key in src) { 
            dest[key] = src[key]; 
        } 
        return dest; 
    } 

    requests.onload = function () {
        var response = this.responseText
        var jsonResponse = JSON.parse(response);
        var accessToken = jsonResponse["access_token"]
        
        
        var userRequests = new XMLHttpRequest();
        userRequests.open('GET', "https://osu.ppy.sh/api/v2/users/" + playerId + "/scores/best?limit=50&offset=0", true)
        userRequests.setRequestHeader("Authorization", "Bearer " + accessToken);
        userRequests.send();

        userRequests.onload = function () {
            var jsonResponse1 = JSON.parse(this.responseText);
            var userRequests2 = new XMLHttpRequest();
            userRequests2.open('GET', "https://osu.ppy.sh/api/v2/users/" + playerId + "/scores/best?limit=50&offset=50", true)
            userRequests2.setRequestHeader("Authorization", "Bearer " + accessToken);
            userRequests2.send();

            userRequests2.onload = function () {
                var jsonResponse2 = JSON.parse(this.responseText);
                var fullScores = extend(jsonResponse2, jsonResponse1)
                //convert legnthCheck to js


            }
        }
    }




    var ringtone = "Amount of Ringtone Sized Maps: 3"
    document.getElementById("osuStats").innerHTML = ringtone
});



