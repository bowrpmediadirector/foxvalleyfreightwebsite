
function toggleNav(){
  const nav = document.getElementById('primary-nav');
  nav.style.display = (nav.style.display === 'block') ? 'none' : 'block';
}
document.addEventListener('DOMContentLoaded', () => {
  const yearEl = document.getElementById('year');
  if(yearEl) yearEl.textContent = new Date().getFullYear();
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Thank you — demo site. Connect a webhook in assets/js/main.js to enable submissions.');
      form.reset();
    });
  });
});
