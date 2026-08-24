let cart = [];
let total = 0;
let currentCategory = 'all';

// --- FILTRARE PRODUSE (CATEGORII ȘI CĂUTARE) ---
function filterCategory(category, event) {
    currentCategory = category;
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');
    filterProducts();
}

function filterProducts() {
    const searchValue = document.getElementById('searchInput').value.toLowerCase();
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        const title = card.querySelector('h3').textContent.toLowerCase();
        const desc = card.querySelector('.desc').textContent.toLowerCase();
        const category = card.getAttribute('data-category');

        const matchesSearch = title.includes(searchValue) || desc.includes(searchValue);
        const matchesCategory = (currentCategory === 'all') || (category === currentCategory);

        if (matchesSearch && matchesCategory) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}

// --- LOGICA PENTRU COȘUL DE CUMPĂRĂTURI ---
function addToCart(nume, pret) {
    cart.push({ nume, pret });
    total += pret;
    updateCartUI();
}

function updateCartUI() {
    const cartItemsList = document.getElementById('cartItems');
    const cartTotalSpan = document.getElementById('cartTotal');

    cartItemsList.innerHTML = '';
    cart.forEach((item) => {
        const li = document.createElement('li');
        li.innerHTML = `<span>${item.nume}</span><span>${item.pret} MDL</span>`;
        cartItemsList.appendChild(li);
    });
    cartTotalSpan.textContent = total;
}

// --- LOGICA PENTRU FEREASTRA DE PLATĂ CU CARDUL ---
function openPaymentModal() {
    if (cart.length === 0) {
        alert("Coșul este gol! Vă rugăm să adăugați produse înainte de a comanda.");
        return;
    }
    // Actualizăm suma totală în fereastra modală
    document.getElementById('modalTotal').textContent = total;
    // Afișăm fereastra
    document.getElementById('paymentModal').style.display = 'flex';
}

function closePaymentModal() {
    document.getElementById('paymentModal').style.display = 'none';
}

function processPayment() {
    // Aici, pe viitor, se va conecta un procesator de plăți real (Stripe, banca etc.)
    // Deocamdată simulăm succesul tranzacției:

    alert("Plata a fost procesată cu succes! Vă mulțumim pentru comanda în valoare de " + total + " MDL.");

    // După plată, golim coșul și închidem fereastra
    cart = [];
    total = 0;
    updateCartUI();
    closePaymentModal();
}

// --- SCHIMBAREA LIMBII ---
function changeLanguage() {
    const lang = document.getElementById('languageSelect').value;
    window.location.href = "/?lang=" + lang;
}