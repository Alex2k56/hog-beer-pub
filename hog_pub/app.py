from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

texte = {
    "ro": {
        "titlu": "MENIU HOG BEER PUB",
        "cauta": "🔍 Caută un produs...",
        "cat_toate": "Toate",
        "cat_bere": "🍺 Bere",
        "cat_cocktailuri": "🍹 Cocktailuri",
        "cat_racoritoare": "🥤 Răcoritoare & Cafea",
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

produse = [
    {
        "id": 1,
        "pret": 45,
        "imagine": "image1.jpg",
        "categorie": "bere",
        "nume": { "ro": "Stella Artois 0.5L", "en": "Stella Artois 0.5L", "ru": "Stella Artois 0.5л" },
        "descriere": { "ro": "Bere blondă premium.", "en": "Premium blonde beer.", "ru": "Светлое пиво премиум-класса." }
    },
    {
        "id": 2,
        "pret": 100,
        "imagine": "image2.jpg",
        "categorie": "cocktailuri",
        "nume": { "ro": "Aperol 450ml", "en": "Aperol 450ml", "ru": "Апероль 450мл" },
        "descriere": { "ro": "Cocktail clasic revigorant.", "en": "Classic refreshing cocktail.", "ru": "Классический освежающий коктейль." }
    }
]

@app.route('/')
def index():
    limba_curenta = request.args.get('lang', 'ru')
    if limba_curenta not in ['ro', 'en', 'ru']:
        limba_curenta = 'ru'

    t = texte[limba_curenta]
    return render_template('index.html', produse=produse, t=t, lang=limba_curenta)

# --- RUTA NOUĂ ADAUGATĂ PENTRU A REZOLVA EROAREA 404 ---
@app.route('/checkout.html')
def checkout_page():
    return render_template('checkout.html')
# -------------------------------------------------------

@app.route('/checkout', methods=['POST'])
def checkout_api():
    data = request.json
    lang = data.get('lang', 'ru')
    mesaj = texte[lang]["mesaj_succes"]
    return jsonify({"status": "success", "message": mesaj})

if __name__ == '__main__':
    # Permite accesul de pe telefon (rețeaua locală)
    app.run(host='0.0.0.0', port=5000, debug=True)
