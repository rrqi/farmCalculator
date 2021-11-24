chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    let url = tabs[0].url;
    if(url.includes("osu.ppy.sh/users")){

    
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
                //var fullScores = extend(jsonResponse2, jsonResponse1)
                fullScores = jsonResponse1.concat(jsonResponse2)
                ringtone = 0
                tvSize = 0
                normal = 0
                long = 0
                marathon = 0

                rtlen = 60
                tvlen = 120
                nmlen = 210
                longlen = 360
                //slack to find where the json stuff gets pulled down. you can remove the comments and correct the naming. <3
                for(i = 0; i < fullScores.length; i++){
                    var item = fullScores[i]
                    var mods = item.mods
                    var exist = false
                    for(j = 0;j < mods.length;j++){
                        var mod = new String(mods[j])
                        if(mod == "DT" || mod == "NC"){
                            exist = true
                        } 
                    }
                    if(exist == true){
                        if(item['beatmap']['total_length'] < rtlen*1.5){
                            ringtone += 1
                        }
                        else if(item['beatmap']['total_length'] < tvlen*1.5){
                            tvSize += 1
                        }
                        else if(item['beatmap']['total_length'] < nmlen*1.5){
                            normal += 1
                        }
                        else if(item['beatmap']['total_length'] < longlen*1.5){
                            long += 1
                        }
                        else{
                            marathon += 1
                        }
                    }
                    else{
                        if(item['beatmap']['total_length'] < rtlen){
                            ringtone += 1
                        }
                        else if(item['beatmap']['total_length'] < tvlen){
                            tvSize += 1
                        }
                        else if(item['beatmap']['total_length'] < nmlen){
                            normal += 1
                        }
                        else if(item['beatmap']['total_length'] < longlen){
                            long += 1
                        }
                        else{
                            marathon += 1
                        }
                    }
                }          
                

                document.getElementById("rtn").innerHTML = "Amount of Ringtone Sized Maps: " + ringtone
                document.getElementById("tvn").innerHTML = "Amount of TV Sized Maps: " + tvSize
                document.getElementById("nmn").innerHTML = "Amount of Medium Sized Maps: " + normal
                document.getElementById("longn").innerHTML = "Amount of Long Sized Maps: " + long
                document.getElementById("elsen").innerHTML = "Amount of Marathon Sized Maps: " + marathon
            }
        }
    }
}
else{
    document.getElementById("rtn").innerHTML = "GO TO AN OSU USERPAGE!!!"
}



});



