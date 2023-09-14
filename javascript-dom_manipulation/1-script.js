const head = document.querySelector('header');
const tag = document.getElementById('red_header');

tag.addEventListener('click', function onClick () {
  head.style.color = '#FF0000';
});
