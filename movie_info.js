/* Gets omdb API query URL like http://www.omdbapi.com/?i=&t=The+Martian */
function getMovieInfoUrl(id) {
    var search_id = id.split(' ').join('+');
    var search_url = "http://www.omdbapi.com/?i=&t=" + search_id;
    console.log(search_url);
    return search_url;
}

/* From http://stackoverflow.com/questions/247483/http-get-request-in-javascript */
function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200) {
            callback(xmlHttp.responseText);
        }
    }
    console.log(theUrl);
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}