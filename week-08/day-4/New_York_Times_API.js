// Search interesting articles on: http://developer.nytimes.com/
//
// Ask your local mentor for the API key or request your own. Use localhost as the website.
//
// Use the Article Search API
// Find articles about the moon landing by Apollo 11
// Display the following fields in a list
// Headline
// Snippet
// Publication date
// Create a permalink to that article
// API key  83356cc0eafb4a60b8849f18c25ca063


var url = 'http://api.giphy.com/v1/gifs/search?q=gandalf&api_key=dc6zaTOxFJmzC&limit=16';

function load(url, callback) {
  var xhr = new XMLHttpRequest();

  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4) {
      console.log(xhr.response); //Outputs a DOMString by default
      let responseFromServer = JSON.parse(xhr.response);
      callback(responseFromServer);
      buildIMG(responseFromServer);
    }
  }

  xhr.open('GET', url, true);
  xhr.send();
}

load(url, function(response){console.log(response)});

function buildIMG (responseFromServer){
    for (let i = 0; i < 16; i++){
        let liElement = document.createElement('li');
        liElement.style.backgroundImage = 'url(' + responseFromServer.data[i].images.downsized_still.url + ')';
        liElement.addEventListener('mouseover', function () {
            this.style.backgroundImage = 'url(' + responseFromServer.data[i].images.downsized_medium.url + ')';
        })
        liElement.addEventListener('mouseleave', function () {
            this.style.backgroundImage = 'url(' + responseFromServer.data[i].images.downsized_still.url + ')';
        })
        ImgContainer.appendChild(liElement);
    }
}

////////////////////////////////////////////////////////////////////////////////

let ImgContainer = document.querySelector('.thumbnail__container');

var url = {
        url: "https://api.nytimes.com/svc/search/v2/articlesearch.json",
        api-key: "83356cc0eafb4a60b8849f18c25ca063",
        q: 'moon'
}

function ajax(url, callback){
     
}


////////////////////////////////////////////////////////////////////////////////

url += '?' + $.param({
  'api-key': "83356cc0eafb4a60b8849f18c25ca063",
  'q': "moon"
});

$.ajax({
  url: url,
  method: 'GET',
}).done(function(result) {
  console.log(result);
}).fail(function(err) {
  throw err;
});
