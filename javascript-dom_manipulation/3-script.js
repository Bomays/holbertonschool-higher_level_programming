document.getElementById('toggle_header').onclick = () => {
  const header = document.querySelector('header');
  header.classList.toggle('green');
  header.classList.toggle('red');
};
