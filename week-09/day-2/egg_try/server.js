'use strict';

var express = require('express');
var app = express();
var five = require('five');

app.get('/', function(req, res){
    res.send({
        name: 'karakter',
        age: 'infinite',
        gender: 'male',
        weapon: req.query.weapon
    });
});

app.get('/five/:lang', function(req, res){
    var lang = req.params.lang;
    var fiveFunc = five[lang];
    res.send(fiveFunc());
});

app.listen(3000);
