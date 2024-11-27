document.addEventListener('DOMContentLoaded', () => {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then((response) => (response.ok ? response.json() : Promise.reject(new Error('Response not ok'))))
    .then((data) => {
      const helloDisplay = data.hello;
      document.getElementById('hello').textContent = helloDisplay;
    })
    .catch((error) => {
      console.error('Fetching error:', error);
    });
});
