from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.form.get("Body", "")
    resp = MessagingResponse()
    resp.message(f"✅ BOT IPO LIVE\nUmetuma: {incoming_msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
