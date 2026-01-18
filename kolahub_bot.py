from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

# WEKA OPENAI API KEY YAKO HAPA
openai.api_key = "sk-XXXXXXX"  # badilisha na API key yako

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    # Chukua message ya WhatsApp
    msg = request.form.get('Body', '').strip()
    resp = MessagingResponse()

    # List ya maneno yanayohusiana na bando/data
    huduma_keywords = [
        "bando", "bundle", "data", "internet", "gb", "halotel",
        "bei", "gharama", "nahitaji", "nataka", "nisaidie", "msaada",
        "nimehitaji", "nipatie", "nimechukua", "ninataka", "mpaka", "tuma",
        "nunua", "kununua", "kuagiza", "sasa", "tafadhali", "omba", "omba kwa", 
        "ninahitaji", "ningependa", "taka", "tunataka", "tunapenda"
    ]

    # Kama message ina maneno yanayohusiana na bando
    if any(word in msg.lower() for word in huduma_keywords):
        # OpenAI prompt
        prompt = f"""
Wewe ni WhatsApp chatbot wa Kola Creative Hub.
Unauza KOLA HALOTEL BUNDLES.

PRICE LIST:
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

MALIPO:
Tuma pesa kwa 0746460472 (Voda) – Asubuh Suba.

Mteja amesema:
"{msg}"

Jibu kwa Kiswahili rahisi, kwa mtindo wa biashara.
Mwelekeze mteja jinsi ya kulipa na aeleze atume jina la Muamala badala ya screenshot.
"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Wewe ni chatbot wa mauzo ya bando za Halotel."},
                    {"role": "user", "content": prompt}
                ]
            )
            reply_text = response['choices'][0]['message']['content']
        except Exception as e:
            reply_text = "Samahani, kuna tatizo kidogo. Jaribu tena baadaye."

        resp.message(reply_text)
    
    # Kama mteja anathibitisha malipo
    elif "nimelipa" in msg.lower() or "nimeshalipa" in msg.lower() or "malipo yametumwa" in msg.lower():
        resp.message(
            "🙏 Asante sana kwa malipo yako.\n"
            "Bando lako linaandaliwa sasa hivi, tafadhali subiri dakika chache.\n"
            "Tunathamini sana kuwa mteja wetu wa Kola Hub! 💛"
        )
    
    # Default reply kwa maneno mengine
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)








