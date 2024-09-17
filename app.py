# app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import spacy

# Initialize Flask application
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chatbot.db'
db = SQLAlchemy(app)

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)

# Initialize the database (creates the tables if they don't exist)
with app.app_context():
    db.create_all()

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([{
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'category': p.category,
            'price': p.price
        } for p in products])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Error handling helper function
def validate_message(message):
    if not message or message.strip() == "":
        return False, "Message cannot be empty!"
    return True, ""

# Route for customer inquiries
@app.route('/inquiry', methods=['POST'])
def handle_inquiry():
    try:
        user_message = request.json.get('message', '')
        is_valid, error_message = validate_message(user_message)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        response = {"response": f"You asked: {user_message}. Here's an answer to your inquiry."}
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for customer complaints
@app.route('/complaint', methods=['POST'])
def handle_complaint():
    try:
        user_message = request.json.get('message', '')
        is_valid, error_message = validate_message(user_message)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        response = {"response": f"We're sorry to hear about your issue: {user_message}. We'll resolve it as soon as possible."}
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route for product recommendations
@app.route('/recommendation', methods=['POST'])
def handle_recommendation():
    try:
        recommended_product = Product.query.first()
        if not recommended_product:
            return jsonify({"error": "No product recommendations available"}), 500

        response = {
            "response": f"We recommend: {recommended_product.name} for ${recommended_product.price}"
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to handle customer messages
@app.route('/process_message', methods=['POST'])
def process_message():
    try:
        data = request.get_json()
        message = data.get('message', '')
        is_valid, error_message = validate_message(message)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        doc = nlp(message)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        response = {
            'original_message': message,
            'entities': entities
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
