document.addEventListener('DOMContentLoaded', () => {
  const appName = document.querySelector('.navbar .navbar-brand')?.textContent?.trim() || 'Gente Control- Gestão de Pessoas e Treinamentos';
  const nameEl = document.getElementById('footer-app-name');
  const yearEl = document.getElementById('footer-year');
  if (nameEl) nameEl.textContent = appName;
  if (yearEl) yearEl.textContent = new Date().getFullYear();
});

// optional: expose a small helper to update footer if needed
window.footer = {
  setAppName(n){ const el = document.getElementById('footer-app-name'); if(el) el.textContent = n; }
};
