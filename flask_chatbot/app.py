from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message'].lower()
    response = generate_response(user_input)
    return response

def generate_response(user_input):
    # Greeting
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! Welcome to Oma Glow Clothing. How can I assist you today?"
    # Basic keywords for a simple chatbot
    elif "recommend" in user_input or "suggest" in user_input:
        return "Sure! What type of clothing are you interested in? (e.g., casual, formal, sportswear)"
    elif "casual" in user_input:
        return "We recommend our comfortable jeans and t-shirts for a casual look. You can find them on our website here: [Oma Glow Casual Collection](https://www.omaglow.com/casual)."
    elif "formal" in user_input:
        return "For a formal look, check out our collection of suits and dresses. Available on our website here: [Oma Glow Formal Collection](https://www.omaglow.com/formal)."
    elif "sportswear" in user_input:
        return "Our sportswear collection includes the latest in activewear. Visit our website here: [Oma Glow Sportswear Collection](https://www.omaglow.com/sportswear)."
    elif "website" in user_input or "site" in user_input:
        return "You can browse our entire collection on our website: [Oma Glow](https://www.omaglow.com)."
    else:
        return "I'm sorry, I didn't understand that. Can you please ask about clothing recommendations or how to visit our website?"

if __name__ == "__main__":
    app.run(debug=True)
