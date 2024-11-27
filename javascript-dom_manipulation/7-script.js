fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then((response) => (response.ok ? response.json() : Promise.reject(new Error('Response not ok'))))
  .then((data) => {
    data.results.forEach((film) => {
      const starWarsFilms = film.title;
      const listItem = document.createElement('li');
      listItem.textContent = starWarsFilms;

      document.getElementById('list_movies').appendChild(listItem);
    });
  })
  .catch((error) => {
    console.error('Fetching error:', error);
  });
