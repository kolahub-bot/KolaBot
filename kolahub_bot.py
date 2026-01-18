from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

# WEKA OPENAI API KEY YAKO HAPA
openai.api_key = "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"

app = Flask(__name__)

from flask import request
from twilio.twiml.messaging_response import MessagingResponse

from flask import request
from twilio.twiml.messaging_response import MessagingResponse

@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get('Body', '').lower()
    resp = MessagingResponse()

    # MANENO YA JUMLA (GENERAL INTENT)
    huduma_keywords = [
        "bando", "bundle", "data", "internet", "gb",
        "halotel", "bei", "gharama", "nahitaji", "nataka",
        "nisaidie", "msaada"
    ]

    # ANGALIA KAMA ANAHITAJI HUDUMA
    if any(word in msg for word in huduma_keywords):

        # GB MAALUM
        if "gb 20" in msg:
            resp.message(
                "✅ GB 20 = 18,000 TSH\n"
                "💳 Lipa: 0746460472 (Voda)\n"
                "📸 Tuma screenshot ya malipo hapa."
            )

        elif "gb 15" in msg:
            resp.message(
                "✅ GB 15 = 13,500 TSH\n"
                "💳 Lipa: 0746460472 (Voda)\n"
                "📸 Tuma screenshot ya malipo hapa."
            )

        elif "gb 10" in msg:
            resp.message(
                "✅ GB 10 = 9,500 TSH\n"
                "💳 Lipa: 0746460472 (Voda)\n"
                "📸 Tuma screenshot ya malipo hapa."
            )

        else:
            # AKITUMIA MANENO YOYOTE YA HUDUMA BILA GB MAALUM
            resp.message(
                "📡 KOLA HALOTEL BUNDLES 🚨\n"
                "GB 6 = 6,000 TSH\n"
                "GB 7 = 7,000 TSH\n"
                "GB 8 = 8,000 TSH\n"
                "GB 9 = 9,000 TSH\n"
                "GB 10 = 9,500 TSH\n"
                "GB 12 = 11,500 TSH\n"
                "GB 15 = 13,500 TSH\n"
                "GB 20 = 18,000 TSH\n\n"
                "✍️ Andika: Nataka GB 20"
            )

    # CONFIRMATION
    elif "nimelipa" in msg or "nimeshalipa" in msg:
        resp.message(
            "🙏 Asante kwa malipo.\n"
            "Bando lako linaandaliwa, tafadhali subiri."
        )

    # DEFAULT (MTU YOYOTE ATAANDIKA CHOCHOTE)
    else:
        resp.message(
            "Karibu Kola Halotel Bundles 😊\n"
            "Andika chochote kama:\n"
            "- bando\n"
            "- nataka data\n"
            "- gb 20\n"
            "- bei ya internet"
        )

    return str(resp)

    prompt = f"""
Wewe ni WhatsApp chatbot wa Kola Creative Hub.
Unauza KOLA HALOTEL BUNDLES.

PRICE LIST:
GB 6 = 6,000 TSH
GB 7 = 7,000 TSH
GB 8 = 8,000 TSH
GB 9 = 9,000 TSH
GB 10 = 9,500 TSH
GB 12 = 11,500 TSH
GB 15 = 13,500 TSH
GB 20 = 18,000 TSH
GB 25 = 23,000 TSH
GB 30 = 27,000 TSH
GB 35 = 30,000 TSH

MALIPO:
Tuma pesa kwa 0746460472 (Voda) – Asubuh Suba.

Mteja amesema:
"{incoming_msg}"

Jibu kwa Kiswahili rahisi, kwa mtindo wa biashara.
Mwelekeze mteja jinsi ya kulipa na aeleze atume kiasi + namba.
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Wewe ni chatbot wa mauzo ya bando za Halotel."},
            {"role": "user", "content": prompt}
        ]
    )

    reply.body(response['choices'][0]['message']['content'])
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





