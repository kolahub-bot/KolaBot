from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

# WEKA OPENAI API KEY YAKO HAPA
openai.api_key = "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"

app = Flask(__name__)

from flask import request
from twilio.twiml.messaging_response import MessagingResponse

@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get('Body', '').lower()
    resp = MessagingResponse()

    huduma_keywords = [
        "bando", "bundle", "data", "internet", "gb", "halotel",
        "bei", "gharama", "nahitaji", "nataka", "nisaidie", "msaada",
        "nimehitaji", "nipatie", "nimechukua", "ninataka", "mpaka", "tuma",
        "nunua", "kununua", "kuagiza", "sasa", "tafadhali", "omba", "omba kwa", 
        "ninahitaji", "ningependa", "taka", "tunataka", "tunapenda"
    ]

    if any(word in msg for word in huduma_keywords):

        if "gb 5" in msg:
            resp.message(
                "✅ GB 5 = 4,500 TSH\n"
                "💳 Lipia kwenye: 0746460472 (Voda)\n"
                "✍️ Baada ya kulipa, tafadhali tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 6" in msg:
            resp.message(
                "✅ GB 6 = 6,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya kulipa, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 7" in msg:
            resp.message(
                "✅ GB 7 = 7,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 8" in msg:
            resp.message(
                "✅ GB 8 = 8,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 10" in msg:
            resp.message(
                "✅ GB 10 = 9,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 12" in msg:
            resp.message(
                "✅ GB 12 = 11,500 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 15" in msg:
            resp.message(
                "✅ GB 15 = 12,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 20" in msg:
            resp.message(
                "✅ GB 20 = 18,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 25" in msg:
            resp.message(
                "✅ GB 25 = 23,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 30" in msg:
            resp.message(
                "✅ GB 30 = 27,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        elif "gb 35" in msg:
            resp.message(
                "✅ GB 35 = 30,000 TSH\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili bando lako liwe active."
            )
        else:
            resp.message(
                "📡 Karibu Kola Halotel Bundles! 😊\n"
                "Hapa ni baadhi ya bando zetu:\n"
                "GB 6 = 6,000 TSH\nGB 7 = 7,000 TSH\nGB 8 = 8,000 TSH\n"
                "GB 10 = 9,000 TSH\nGB 12 = 11,500 TSH\nGB 15 = 12,000 TSH\nGB 20 = 18,000 TSH\n"
                "Andika tu: Nataka GB 10 (au yoyote unayohitaji)\n"
                "💳 Lipia: 0746460472 (Voda)\n"
                "✍️ Baada ya malipo, tuma **jina la Muamala** ili tukuthibitishie bando lako."
            )

    elif "nimelipa" in msg or "nimeshalipa" in msg or "malipo yametumwa" in msg:
        resp.message(
            "🙏 Asante sana kwa malipo yako.\n"
            "Bando lako linaandaliwa sasa hivi, tafadhali subiri dakika chache.\n"
            "Tunathamini sana kuwa mteja wetu wa Kola Hub! 💛"
        )

    else:
        resp.message(
            "Karibu Kola Halotel Bundles! 😊\n"
            "Andika maneno yoyote yanayohusiana na:\n"
            "- bando\n- data\n- GB\n- internet\n- halotel\n"
            "Mfano: 'Nataka GB 20' au 'Nahitaji bando'\n"
            "💳 Lipia: 0746460472 (Voda)\n"
            "✍️ Baada ya malipo, tuma **jina la Muamala** ili tukuthibitishie bando lako."
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







