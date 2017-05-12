// Display gifs of a cute/funny topic using: https://github.com/Giphy/GiphyAPI
//
// Search/Find the images in the API
// Display the list of the first 16 results's static thumbnail
// If the user clicks on the thumbnail, display the animated GIF

let ImgContainer = document.querySelector('.thumbnail__container');
let searchInput = document.querySelector('#search');
let searchBar = document.querySelector('#searchbar');
let searchFunction = document.querySelector('#search');
const listOfKeyCodes = [81, 86, 69, 82, 84, 89, 91, 89, 85, 73, 79, 80, 219, 91, 221, 65, 83, 68, 70, 91, 71, 72, 74, 75, 76, 186, 222, 220, 192, 90, 88]
const listOfKeyCodes2 = [67, 66, 78, 77, 188, 190, 191]
const colorCodes = ['#E389F5', '#15D549', '#FFF928', '#09C6FF', '#FFFFFF'];
let colorCodesIndex = 0;



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
            console.log(ImgContainer.innerHTML);
        })
        liElement.addEventListener('mouseleave', function () {
            this.style.backgroundImage = 'url(' + responseFromServer.data[i].images.downsized_still.url + ')';
        })
        ImgContainer.appendChild(liElement);
    }
}

searchInput.addEventListener('keyup', function(e) {
    if (e.keyCode == 13) { // ENTER key
        url = 'http://api.giphy.com/v1/gifs/search?q=' + searchInput.value + '&api_key=dc6zaTOxFJmzC&limit=16';
        console.log(url);
        ImgContainer.innerHTML = "";
        console.log(ImgContainer.innerHTML);
        load(url, function(response){console.log(response)});
        console.log(searchInput.value)
    }
} )

searchInput.addEventListener('keyup', function(e) {
    // console.log(e.keyCode);
    colorCodesIndex++;
    if (listOfKeyCodes.includes(e.keyCode) || listOfKeyCodes.includes(e.keyCode)){
        console.log(e)

        searchBar.style.background = colorCodes[colorCodesIndex % colorCodes.length - 1];
        searchFunction.style.background = colorCodes[colorCodesIndex % colorCodes.length - 1];
    }
})
