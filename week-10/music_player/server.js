'use strict';

const express = require('express');
const mysql = require('mysql');

const app = express();

const conn = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'MusicPlayer'
});

conn.connect(err => {
    if(err){
        console.log('Error connecting to database');
    }
    console.log('Connection established\n');
});

let playlistData;
let tracksData;

app.use('/assets', express.static('assets'));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/playlists', (req, res) => {
    conn.query('SELECT * FROM Playlist', (err, rows) => {
        if (err) {
            console.log('Error: ', err);
        } else {
            playlistData = rows;
        }
        res.send(playlistData);
    });
});

app.get('/playlists-tracks', (req, res) => {
    conn.query('SELECT * FROM Tracks', (err, rows) => {
        if (err) {
            console.log('Error: ', err);
        } else {
            tracksData = rows;
            console.log(rows)
            console.log(tracksData)

        }
        res.send(tracksData)
    });
});

app.listen(3000, () => {
    console.log('server is running');
});
