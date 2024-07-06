from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot_response(userText))

def bot_response(message):
    # Simple chatbot logic for Oma Glow
    message = message.lower()
    if 'hello' in message or 'hi' in message:
        return "Hello! Welcome to Oma Glow. How can I assist you today?"
    elif 'products' in message:
        return "We offer a wide range of skincare and beauty products including moisturizers, serums, and makeup. What specific product are you interested in?"
    elif 'recommend' in message:
        return "Sure! Could you please tell me your skin type (e.g., oily, dry, combination)?"
    elif 'oily' in message:
        return "For oily skin, I recommend our Oil-Free Moisturizer and Clarifying Cleanser."
    elif 'dry' in message:
        return "For dry skin, I recommend our Hydrating Serum and Ultra Rich Moisturizer."
    elif 'combination' in message:
        return "For combination skin, I recommend our Balancing Toner and Lightweight Moisturizer."
    elif 'buy' in message:
        return "You can purchase our products directly from our website at oma-glow.com."
    elif 'contact' in message:
        return "You can reach our customer service at support@oma-glow.com or call us at 123-456-7890."
    elif 'bye' in message or 'goodbye' in message:
        return "Goodbye! Thank you for visiting Oma Glow. Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please provide more details or ask another question?"

if __name__ == "__main__":
    app.run(debug=True)
