('use strict');


const express = require('express');
const app = express();

app.use('/assets', express.static('assets'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
})

app.get('/doubling', function(req, res){
    var received = Math.floor(req.query.input);
    // var received = Math.floor(received);
    console.log(received)

    var result = function() {
        if (received) {
            console.log('eljut ide, csak kezdeni nem tud mit vele a gyoker')
            return {
                  received: received,
                  result: received * 2
                }
        } else {
            console.log('Valamiert ez a szar, error-t akar dobni mert a !received if aktivalodik')
            return {
                "error": "Please provide an input!"
                }
            }
    }
    res.send(result());
})

app.listen(8080, function(){
    console.log('server up and running')
});
