fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then((response) => (response.ok ? response.json() : Promise.reject(new Error('Response not ok'))))
  .then((data) => {
    const characterName = data.name;
    document.getElementById('character').textContent = characterName;
  })
  .catch((error) => {
    console.error('Fetching error:', error);
  });
