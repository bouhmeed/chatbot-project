from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AI-Powered Customer Support Chatbot!"

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    user_message = data.get('message')
    # For now, we'll just return the message back
    return jsonify({"response": f"Received your message: {user_message}"})

if __name__ == '__main__':
    app.run(debug=True)
