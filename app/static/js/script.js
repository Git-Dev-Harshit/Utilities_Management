window.addEventListener('load', function () {
  document.querySelectorAll('nav a').forEach(link => {
    link.classList.add('visible');
  });
  document.querySelector('.brand').classList.add('visible');
  // You can do this for other elements as needed
});
