async function swCharacterName() {
    let response = await fetch("https://swapi-api.hbtn.io/api/films/?=json");
    const movies = await response.json();

    
    let films = movies.results

    films.forEach(film => {
        let parrafo = document.createElement('li');
        let text = document.createTextNode(film.title);
        parrafo.appendChild(text);
        document.querySelector('#list_movies').appendChild(parrafo);
    });
}

swCharacterName();