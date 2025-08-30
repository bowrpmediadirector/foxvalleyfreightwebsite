
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('form').forEach(f => {
    f.addEventListener('submit', (e) => {
      e.preventDefault();
      alert('Form submitted (demo). Hook up your webhook or server to process forms.');
      f.reset();
    });
  });
});
