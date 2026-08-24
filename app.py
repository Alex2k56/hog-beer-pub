# --- TRADUCERILE PENTRU INTERFAȚĂ ---
texte = {
    "ro": {
        "titlu": "MENIU HOG BEER PUB",
        "cauta": "🔍 Caută un produs...",
        "cat_toate": "Toate",
        "cat_bere": "🍺 Bere",
        "cat_cocktailuri": "🍹 Cocktailuri",
        "cat_racoritoare": "🥤 Răcoritoare",
        "cat_gustari": "🍟 Gustări",
        "cat_mancare": "🍔 Fel Principal",
        "cat_desert": "🍦 Desert",
        "cos_titlu": "🛒 Coșul tău",
        "total": "Total:",
        "buton_comanda": "Comandă",
        "buton_adauga": "Adaugă",
        "mesaj_succes": "Vă mulțumim! Comanda a fost preluată."
    },
    "en": {
        "titlu": "HOG BEER PUB MENU",
        "cauta": "🔍 Search...",
        "cat_toate": "All",
        "cat_bere": "🍺 Beer",
        "cat_cocktailuri": "🍹 Cocktails",
        "cat_racoritoare": "🥤 Soft Drinks",
        "cat_gustari": "🍟 Snacks",
        "cat_mancare": "🍔 Main Courses",
        "cat_desert": "🍦 Dessert",
        "cos_titlu": "🛒 Your Cart",
        "total": "Total:",
        "buton_comanda": "Order",
        "buton_adauga": "Add",
        "mesaj_succes": "Thank you! Order received."
    },
    "ru": {
        "titlu": "МЕНЮ HOG BEER PUB",
        "cauta": "🔍 Поиск...",
        "cat_toate": "Все",
        "cat_bere": "🍺 Пиво",
        "cat_cocktailuri": "🍹 Коктейли",
        "cat_racoritoare": "🥤 Напитки",
        "cat_gustari": "🍟 Закуски",
        "cat_mancare": "🍔 Горячие блюда",
        "cat_desert": "🍦 Десерты",
        "cos_titlu": "🛒 Ваша корзина",
        "total": "Итого:",
        "buton_comanda": "Заказать",
        "buton_adauga": "Добавить",
        "mesaj_succes": "Спасибо! Ваш заказ принят."
    }
}

# --- BAZA DE DATE CU PRODUSE (CU ML/GRAME) ---
produse = [
    # --- BERE ---
    {
        "id": 1,
        "pret": 45,
        "imagine": "stella_sticla.jpg",
        "categorie": "bere",
        "nume": {"ro": "Stella Artois 500ml", "en": "Stella Artois 500ml", "ru": "Stella Artois 500мл"},
        "descriere": {"ro": "Bere blondă premium la sticlă.", "en": "Premium blonde bottled beer.",
                      "ru": "Светлое пиво премиум-класса в бутылке."}
    },
    {
        "id": 2,
        "pret": 40,
        "imagine": "corona.jpg",
        "categorie": "bere",
        "nume": {"ro": "Corona Extra 330ml", "en": "Corona Extra 330ml", "ru": "Corona Extra 330мл"},
        "descriere": {"ro": "Bere mexicană servită cu lime.", "en": "Mexican beer served with lime.",
                      "ru": "Мексиканское пиво с лаймом."}
    },

    # --- COCKTAILURI ---
    {
        "id": 3,
        "pret": 100,
        "imagine": "aperol.jpg",
        "categorie": "cocktailuri",
        "nume": {"ro": "Aperol Spritz 450ml", "en": "Aperol Spritz 450ml", "ru": "Апероль 450мл"},
        "descriere": {"ro": "Aperol, prosecco, apă minerală, portocală.",
                      "en": "Aperol, prosecco, sparkling water, orange.",
                      "ru": "Апероль, просекко, минеральная вода, апельсин."}
    },
    {
        "id": 4,
        "pret": 70,
        "imagine": "mojito.jpg",
        "categorie": "cocktailuri",
        "nume": {"ro": "Mojito Clasic 350ml", "en": "Classic Mojito 350ml", "ru": "Мохито Классический 350мл"},
        "descriere": {"ro": "Rom, mentă proaspătă, lime, zahăr.", "en": "Rum, fresh mint, lime, sugar.",
                      "ru": "Ром, свежая мята, лайм, сахар."}
    },

    # --- GUSTĂRI ---
    {
        "id": 5,
        "pret": 165,
        "imagine": "creveti_usturoi.jpg",
        "categorie": "gustari",
        "nume": {"ro": "Creveți prăjiți cu usturoi 280g", "en": "Fried shrimp with garlic 280g",
                 "ru": "Креветки жареные с чесноком 280г"},
        "descriere": {"ro": "Creveți mărimea 20/30 trași la tigaie.", "en": "20/30 pan-fried shrimp.",
                      "ru": "Креветки 20/30 обжаренные на сковороде."}
    },
    {
        "id": 6,
        "pret": 30,
        "imagine": "cartofi_fri.jpg",
        "categorie": "gustari",
        "nume": {"ro": "Cartofi Fri 150g", "en": "French Fries 150g", "ru": "Картофель фри 150г"},
        "descriere": {"ro": "Cartofi prăjiți crocanți, aurii.", "en": "Crispy golden french fries.",
                      "ru": "Хрустящий золотистый картофель фри."}
    },

    # --- FEL PRINCIPAL ---
    {
        "id": 7,
        "pret": 140,
        "imagine": "burger_vita.jpg",
        "categorie": "fel_principal",
        "nume": {"ro": "Burger de Vită (350g) + Cartofi (150g)", "en": "Beef Burger (350g) + Fries (150g)",
                 "ru": "Бургер говяжий (350г) + картошка фри (150г)"},
        "descriere": {"ro": "Burger suculent servit cu garnitură.", "en": "Juicy burger served with fries.",
                      "ru": "Сочный бургер с картофелем фри."}
    },

    # --- DESERT ---
    {
        "id": 8,
        "pret": 25,
        "imagine": "inghetata.jpg",
        "categorie": "desert",
        "nume": {"ro": "Înghețată 50g (1 bilă)", "en": "Ice Cream 50g (1 scoop)", "ru": "Мороженое 50г (1 шарик)"},
        "descriere": {"ro": "Arome variate la alegere.", "en": "Various flavors to choose from.",
                      "ru": "Различные вкусы на выбор."}
    }
]