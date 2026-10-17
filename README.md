# 🍺 Hog Beer Pub — A Casual Front-End Project

<img width="1837" height="812" alt="Captură de ecran 2026-08-22 125707" src="https://github.com/user-attachments/assets/13278a02-51a7-46e9-be71-41f908b209dd" />
<img width="1855" height="875" alt="Captură de ecran 2026-08-22 125914" src="https://github.com/user-attachments/assets/7baa8eb5-0ca9-4d39-ac27-153c12d04829" />
<img width="1866" height="852" alt="Captură de ecran 2026-08-22 125923" src="https://github.com/user-attachments/assets/37eda982-c853-446a-8b40-93ab45e0857f" />






This is a personal web project I built for a craft beer pub. The goal was simple: create a clean, responsive, and ultra-fast web page where customers can quickly check what's on tap, browse food options, and book a table without loading a heavy PDF or navigating through a slow WordPress site.

---

## 💡 The Story Behind the Project

Most local pub websites suffer from two main issues:
1. They force users to download massive PDF menus on mobile data.
2. They use heavy frameworks for simple layouts, making page loads unnecessarily slow.

I built **Hog Beer Pub** using plain, native web tech (HTML, CSS, Vanilla JavaScript). It loads instantly, works smoothly on mobile screens, and gives patrons exactly what they need in a few clicks.

---

## 🛠️ How It's Built

Instead of reaching for heavy libraries, I kept things lightweight and clean:

- **Semantic HTML5:** Built for readability, proper DOM structure, and clean SEO.
- **Custom CSS3:** Uses CSS Variables for colors/fonts, and Flexbox/Grid for a mobile-first responsive layout.
- **Vanilla JS (ES6+):** Light scripts for the mobile menu toggle, drink category filtering, and simple form validation.

---

## 💻 A Quick Look Under the Hood

Here is how a couple of core features are implemented in code:

### 1. Instant Category Filter (No Page Reloads)
Using `data-` attributes on menu items, users can toggle between draft beers, food, and specials instantly:

```javascript
// Dynamic menu filter
const filterBtns = document.querySelectorAll('.filter-btn');
const menuItems = document.querySelectorAll('.menu-item');

filterBtns.forEach(btn => {
  btn.addEventListener('click', (e) => {
    // Update active tab styling
    document.querySelector('.filter-btn.active')?.classList.remove('active');
    e.target.classList.add('active');

    const category = e.target.dataset.category;

    menuItems.forEach(item => {
      const match = category === 'all' || item.dataset.category === category;
      item.style.display = match ? 'block' : 'none';
    });
  });
});




