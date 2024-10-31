// script.js
function toggleDarkMode() {
    const isDark = document.body.classList.toggle("dark-mode");
        document.cookie = `darkmode=${isDark}; path=/;`;
        }