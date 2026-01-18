from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os

# CHUKUA OPENAI KEY KUTOKA ENVIRONMENT
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get("Body", "").strip().lower()
    resp = MessagingResponse()

    # MANENO YOTE YANAYOWEZA KUOMBA BANDO (KAMILI SANA)
    huduma_keywords = [
        "bando", "bando zako", "bando halotel", "halotel",
        "data", "internet", "gb", "bundle", "bundles",
        "nahitaji", "ninahitaji", "nataka", "ningependa",
        "nisaidie", "msaada", "naomba", "tafadhali",
        "niuzie", "nipe", "nipatie", "nunua", "kununua",
        "kuagiza", "order", "bei", "gharama", "price",
        "mpango", "paketi", "pakage", "package",
        "leo", "sasa", "haraka", "muda huu",
        "gb ngapi", "bando ngapi", "nitapata",
        "natuma pesa", "nikilipia", "nikilipa",
        "unauzaje", "unauza", "mna bando",
        "salio", "line", "lain", "simu",
        "nifanyie", "niwekee", "niunganishie"
    ]

    # KAMA NI MAOMBI YA BANDO → TUMIA AI
    if any(word in msg for word in huduma_keywords):

        prompt = f"""
Wewe ni WhatsApp chatbot wa Kola Creative Hub.
Lengo lako ni kuhudumia wateja wa bando za Halotel kwa upole, heshima na lugha safi ya Kiswahili.

📦 KOLA HALOTEL BUNDLES (BEI):
GB 5 = 4,500 TSH
GB 6 = 6,000 TSH
GB 7 = 7,000 TSH
GB 8 = 8,000 TSH
GB 10 = 9,000 TSH
GB 12 = 11,500 TSH
GB 15 = 12,000 TSH
GB 20 = 18,000 TSH
GB 25 = 23,000 TSH
GB 30 = 27,000 TSH
GB 35 = 30,000 TSH

💳 MALIPO:
Tuma pesa kwa namba: 0746460472 (Voda)
Jina: Asubuh Suba

📌 MUHIMU:
Baada ya kulipa, mteja **atume jina la Muamala** (si screenshot).

Mteja ameandika:
"{msg}"

👉 Jibu kwa Kiswahili kizuri, cha biashara,
👉 Mkaribishe kwa upole,
👉 Mwelekeze achague GB,
👉 Eleza malipo,
👉 Mkumbushe atume jina la Muamala.
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Wewe ni msaidizi wa mauzo ya bando za Halotel."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply_text = response["choices"][0]["message"]["content"]
        except Exception:
            reply_text = (
                "Samahani, kuna changamoto ya mtandao kwa sasa.\n"
                "Tafadhali jaribu tena baada ya muda mfupi 🙏"
            )

        resp.message(reply_text)

    # KAMA MTEJA ANATHIBITISHA MALIPO
    elif any(word in msg for word in ["nimelipa", "nimeshalipa", "tayari nimelipa", "malipo yametumwa", "nimesha tuma pesa"]):
        resp.message(
            "🙏 Asante sana kwa malipo yako.\n"
            "Tafadhali tuma **jina la Muamala** ili tukuhakikishie bando lako mara moja.\n"
            "Ahsante kwa kuchagua Kola Creative Hub 💛"
        )

    # DEFAULT MESSAGE
    else:
        resp.message(
            "👋 Karibu Kola Halotel Bundles!\n\n"
            "Andika kwa uhuru kabisa mfano:\n"
            "• Nataka GB 10\n"
            "• Naomba bando la halotel\n"
            "• Nisaidie bando la internet\n\n"
            "💳 Malipo: 0746460472 (Voda)\n"
            "✍️ Baada ya kulipa, tuma **jina la Muamala**."
        )

    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)









