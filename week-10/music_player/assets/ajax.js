var url = 'http://localhost:3000/playlists'
const playlist = document.querySelector('.playlists_name');

const getPlaylists = function(callback) {
    const endpoint = 'http://localhost:3000/playlists';
    callback(endpoint, function(playData){
        renderPlaylists(playData)
    })
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
    let output = Mustache.render('{{#tracks}} <li class="list_name"><p>{{title}}</p><span class="list_deleter"></span></li> {{/tracks}}', {tracks:playData});
    console.log({tracks:playData});
    console.log(output);
    playlist.innerHTML = output;
}

getPlaylists(ajax)
