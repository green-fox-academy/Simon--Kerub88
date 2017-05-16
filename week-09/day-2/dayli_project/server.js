('use strict');


const express = require('express');
const app = express();

app.use('/assets', express.static('assets'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
})

app.get('/doubling', function(req, res){
    var received = Math.floor(req.query.input);
    console.log(received)

    var result = function() {
        if (received) {
            return {
                  received: received,
                  result: received * 2
                }
        } else {
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
