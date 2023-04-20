var addMoviesToDom = function(movies) {
    const moviesList = document.getElementById("navigation-list");
    
    const listItems = movies.map((movie) => {

        var listItem = document.createElement("li");

        var image = document.createElement("img");
        image.src = movie.Poster;

        var link = document.createElement("a");
        link.href = "https://www.imdb.com/title/" + movie.imdbID;
        link.target = "_blank";

        listItem.appendChild(link);
        link.appendChild(image);

        return listItem;
    
    });

    listItems.forEach(listItem => {
        moviesList.appendChild(listItem);
        
    });
};

addMoviesToDom(movieDB.Movies);

function removeMoviesFromDOM() {
    const currentListedMovies = document.getElementById("navigation-list");

    while (currentListedMovies.hasChildNodes()) {
        currentListedMovies.removeChild(currentListedMovies.firstChild);

    };
}


function addEventListeners() {
    const radioButtons = document.getElementsByName("film-filter");

    radioButtons.forEach((radioButton) => {
        radioButton.addEventListener("change", handleOnChangeEvent);
    });
}


function filterMoviesOnTitle(wordInMovieTitle) {
    removeMoviesFromDOM();

    const filterMovies = movieDB.Movies
        .filter((movie) => {
            return movie.Title.includes(wordInMovieTitle);
        });

    addMoviesToDom(filterMovies);
}


function filterLatestMovies() {
    removeMoviesFromDOM();

    const filterMoviesYear = movieDB.Movies
        .filter((movie) => {
            return movie.Year >= 2014;
        });

    addMoviesToDom(filterMoviesYear);
}


function handleOnChangeEvent(event) {
    switch (event.target.value) {
        case "lastmovies":
            filterLatestMovies();
            break;
        case "avenger":
            filterMoviesOnTitle("Avenger");
            break;
        case "xmen":
            filterMoviesOnTitle("X-Men");
            break;
        case "princess":
            filterMoviesOnTitle("Princess");
            break;
        case "batman":
            filterMoviesOnTitle("Batman");
            break;
        default:
            console.log("geen idee welke film");
            break;
    }
}


addEventListeners();