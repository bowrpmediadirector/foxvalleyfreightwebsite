
function toggleNav(){
  const nav = document.getElementById('primary-nav');
  nav.style.display = (nav.style.display === 'block') ? 'none' : 'block';
}
document.addEventListener('DOMContentLoaded', () => {
  const yearEl = document.getElementById('year');
  if(yearEl){ yearEl.textContent = new Date().getFullYear(); }

  // Example: send forms to a Discord webhook (replace URL below).
  const webhookURL = ''; // paste your Discord webhook URL here to enable
  document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', async (e) => {
      if(!webhookURL){ return; } // fallback to normal submission if no webhook
      e.preventDefault();
      const data = new FormData(form);
      const payload = {
        content: '**New Website Submission**',
        embeds: [{
          title: document.title,
          fields: Array.from(data.entries()).map(([name, value]) => ({ name, value: String(value).slice(0, 1024) }))
        }]
      };
      try{
        await fetch(webhookURL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        alert('Thanks! Your submission was sent.');
        form.reset();
      }catch(err){
        console.error(err);
        alert('Could not send. Please try again later.');
      }
    });
  });
});
