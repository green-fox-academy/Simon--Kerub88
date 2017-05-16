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

app.get('/greeter', function(req, res){
    const name = req.query.name;
    console.log(name);
    const title = req.query.title;
    console.log(title);

    let greet = function(){
        if (name && title){
            return {welcome_message: "Oh, hi there " + name + ", my dear " + title + "!"}
        }else if (name === undefined){
            return {error: "Please provide a name!"}
        }else if (title === undefined){
            return {error: "Please provide a title!"}
        }
    }
    res.send(greet());
})

// app.get('/appenda', function(req, res){
//     const name = req.query.name;
//     console.log(name);
//     const title = req.query.title;
//     console.log(title);
//
//     let greet = function(){
//         if
//     }
//     res.send(greet());
// })

app.get('/appenda/:id', function(req, res) {
    let appendFun = function(){
        return {
            appended: req.params.id + 'a'
        }
    }
    res.send(appendFun());
});


app.listen(8080, function(){
    console.log('server up and running')
});
