'use strict';


const PlayerControll = function() {
    console.log('alive')

    var trackOnClick = function(tracksData) {
        console.log('elek')
        let trackList = document.querySelectorAll('#playlist li');
        trackList.forEach((track, i) => {
            track.addEventListener('click', () => {
                console.log(tracksData[i].path);
                albumCover(tracksData[i]);
                changeSong(tracksData[i]);
                albumTitleAndArtist(tracksData[i])
            });
        });
    };

    const changeSong = function(trackData) {
        const audio = document.querySelector('.audio');
        audio.setAttribute('src', trackData.path);
        audio.play()
    };

    const albumCover = function(trackData) {
        const cover = document.querySelector('.cover_art');
        console.log(trackData)
        cover.style.backgroundImage = 'url(' + trackData.album_artwork + ')';
    };

    const albumTitleAndArtist = function(trackData) {
        const albumTitle = document.querySelector('.album_title h2');
        const artistName = document.querySelector('.artist_name h3');
        albumTitle.innerHTML = trackData.album;
        artistName.innerHTML = trackData.artist;
    }

    return {
        trackOnClick: trackOnClick
    };
};
