var url = 'http://localhost:3000/playlists'
const playlist = document.querySelector('.playlists_name');

var getPlaylists = function(callback){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);


    xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var tracks = JSON.parse(xhr.response);
        // for (let i = 0; i < fullDataArray.posts.length; i++) {
        //     postCreate(fullDataArray.posts[i]);
        // }
        callback(tracks)
    }
    }
    xhr.send()
}

var printData = function(data){
    console.log(data);
    renderPlaylists(data);
}

var renderPlaylists = function(resp) {
    let output = Mustache.render('{{#tracks}} <li class="list_name"><p>{{title}}</p><span class="list_deleter"></span></li> {{/tracks}}', {tracks:resp});
    console.log({tracks:resp});
    console.log(output);
    playlist.innerHTML = output;
}

getPlaylists(printData)
