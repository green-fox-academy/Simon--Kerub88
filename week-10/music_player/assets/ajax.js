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
    let output = Mustache.render('{{#playlists}} <li class="list_name"><p>{{title}}</p><span class="list_deleter"></span></li> {{/playlists}}', {playlists:playData});
    playlist.innerHTML = output;
}

var renderTracks = function(playData) {
    console.log(playData)
    console.log({tracks:playData})
    let output = Mustashe.render('{{#tracks}} <li><a href="{{path}}"><p>{{title}}</p></a><span>{{duration}}</span></li> {{/tracks}}', {tracks:playData});
    tracklist.innerHTML = output;

}

getPlaylists(ajax)
getTracks(ajax)
