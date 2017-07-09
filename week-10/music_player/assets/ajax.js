var url = 'http://localhost:3000/playlists'
const playlist = document.querySelector('.playlists_name');
const tracklist = document.querySelector('#playlist');

const getPlaylists = function(callback) {
    const endpoint = 'http://localhost:3000/playlists';
    callback(endpoint, renderPlaylists);
}

const getTracks = function(callback) {
    const endpoint = 'http://localhost:3000/playlists-tracks';
    callback(endpoint, renderTracks);
}

var ajax = function(url, callback){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            var playData = JSON.parse(xhr.response);
            callback(playData)
        }
    }
    xhr.send()
}

var renderPlaylists = function(playData) {
    for (let i = 0; i < playData.length; i++) {
        if (playData[i].system !== 1) {
            let newPlayList = '<li class="list_name"><p>' + playData[i].title + '</p><span class="list_deleter">✖︎</span></li>'
            playlist.innerHTML = newPlayList;
        }
    }
}

var renderTracks = function(playData) {
    let output = Mustache.render('{{#tracks}} <li><article href="{{path}}"><p>{{title}}</p></article><span><p>{{duration}}</p></span></li> {{/tracks}}', {tracks:playData});
    tracklist.innerHTML = output;
    let PC = PlayerControll()
    PC.trackOnClick(playData);
}

getPlaylists(ajax)
getTracks(ajax)
