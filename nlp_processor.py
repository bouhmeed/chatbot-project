# nlp_processor.py
import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

def process_message(message):
    doc = nlp(message)
    # Example: Simple categorization based on keywords
    if "complaint" in message.lower():
        return "complaint"
    elif "recommend" in message.lower() or "suggest" in message.lower():
        return "recommendation"
    else:
        return "inquiry"
