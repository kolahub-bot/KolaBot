from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get("Body", "").lower()
    resp = MessagingResponse()

    # MANENO YOTE YANAYOWEZA KUTUMIWA KUOMBA HUDUMA
    keywords = [
        "bando", "bundle", "data", "internet", "gb", "halotel",
        "bei", "gharama", "price", "nunua", "nununue", "ninunulie",
        "nahitaji", "ninahitaji", "nataka", "ningependa", "omba",
        "msaada", "help", "nisaidie", "tuma", "nipe", "nipatie",
        "pakiti", "ofaa", "menu", "option", "chaguo", "sasa",
        "leo", "haraka", "tafadhali"
    ]

    # MANENO YA MALIPO
    paid_words = [
        "nimelipa", "nimeshalipa", "tayari nimelipa",
        "malipo yametumwa", "nimetuma pesa", "imetumwa",
        "nishalipa", "nimelipia"
    ]

    # BEI ZA BAND0
    prices = {
        "gb 5": "GB 5 = 5,500 TSH",
        "gb 6": "GB 6 = 6,000 TSH",
        "gb 7": "GB 7 = 7,000 TSH",
        "gb 8": "GB 8 = 8,000 TSH",
        "gb 10": "GB 10 = 9,000 TSH",
        "gb 12": "GB 12 = 11,500 TSH",
        "gb 15": "GB 15 = 12,000 TSH",
        "gb 20": "GB 20 = 18,000 TSH",
        "gb 25": "GB 25 = 23,000 TSH",
        "gb 30": "GB 30 = 27,000 TSH",
        "gb 35": "GB 35 = 30,000 TSH"
    }

    # 1️⃣ AKISEMA AMELIPA
    if any(word in msg for word in paid_words):
        resp.message(
            "🙏 Asante sana kwa malipo yako.\n\n"
            "Tafadhali tuma **JINA LA MUAMALA** ili tukuthibitishie na "
            "kukuwekea bando lako haraka.\n\n"
            "Asante kwa kuchagua *Kola Halotel Bundles* 💛"
        )
        return str(resp)

    # 2️⃣ AKIOMBA BAND0 MAALUM
    for key, value in prices.items():
        if key in msg:
            resp.message(
                f"✅ {value}\n\n"
                "💳 LIPA KUPITIA:\n"
                "0746460472 (Voda) – Asubuh Suba\n\n"
                "✍️ Baada ya malipo, tafadhali tuma **JINA LA MUAMALA** "
                "ili bando lako liwekwe mara moja 🚀"
            )
            return str(resp)

    # 3️⃣ AKITUMA UJUMBE WOWOTE WA HUDUMA
    if any(word in msg for word in keywords):
        resp.message(
            "🌟 Karibu *Kola Halotel Bundles* 😊\n\n"
            "📡 BAND0 ZETU:\n"
            "GB 6 = 6,000 TSH\n"
            "GB 7 = 7,000 TSH\n"
            "GB 8 = 8,000 TSH\n"
            "GB 10 = 9,000 TSH\n"
            "GB 12 = 11,500 TSH\n"
            "GB 15 = 12,000 TSH\n"
            "GB 20 = 18,000 TSH\n"
            "GB 25 = 23,000 TSH\n"
            "GB 30 = 27,000 TSH\n"
            "GB 35 = 30,000 TSH\n\n"
            "👉 Andika mfano: *Nataka GB 10*\n\n"
            "💳 Malipo: 0746460472 (Voda)\n"
            "✍️ Baada ya kulipa, tuma **JINA LA MUAMALA**"
        )
        return str(resp)

    # 4️⃣ UJUMBE USIOELEWEKA
    resp.message(
        "👋 Karibu Kola Halotel Bundles!\n\n"
        "Tafadhali andika ujumbe unaohusiana na:\n"
        "👉 bando / GB / internet / halotel\n\n"
        "Mfano: *Nahitaji GB 15*\n"
        "Tutakuhudumia mara moja 😊"
    )
    return str(resp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
