from textblob import TextBlob
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data['text']
    blob = TextBlob(text)
    return jsonify({
        "French": str(blob.translate(to='fr')),
        "Spanish": str(blob.translate(to='es')),
        "German": str(blob.translate(to='de'))
    })

@app.route('/analyze_sentences', methods=['POST'])
def analyze_sentences():
    sentences = request.json['sentences']
    results = []
    for sent in sentences:
        blob = TextBlob(sent)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        results.append({
            "sentence": sent,
            "polarity": polarity,
            "subjectivity": subjectivity,
            "polarity_label": "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral",
            "subjectivity_label": "subjective" if subjectivity > 0.5 else "objective"
        })
    return jsonify(results)

@app.route('/paragraph_sentiment', methods=['POST'])
def paragraph_sentiment():
    para = request.json['paragraph']
    blob = TextBlob(para)
    return jsonify([
        {"sentence": str(sent), "polarity": TextBlob(str(sent)).sentiment.polarity}
        for sent in blob.sentences
    ])

@app.route('/pos_tags', methods=['POST'])
def pos_tags():
    text = request.json['sentence']
    blob = TextBlob(text)
    return jsonify(blob.tags)

@app.route('/spell_check', methods=['POST'])
def spell_check():
    word = request.json['word']
    blob = TextBlob(word)
    correct = blob.correct()
    suggestions = blob.spellcheck()[:3]
    return jsonify({
        "corrected": str(correct),
        "suggestions": suggestions
    })

@app.route('/extract_adjectives', methods=['POST'])
def extract_adjectives():
    para = request.json['paragraph']
    blob = TextBlob(para)
    adjectives = [word for word, tag in blob.tags if tag == 'JJ']
    return jsonify(adjectives)

@app.route('/noun_phrases', methods=['POST'])
def noun_phrases():
    text = request.json['text']
    blob = TextBlob(text)
    phrases = blob.noun_phrases
    freq = {}
    for phrase in phrases:
        freq[phrase] = freq.get(phrase, 0) + 1
    top_phrases = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
    return jsonify([phrase for phrase, _ in top_phrases])

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json['text']
    blob = TextBlob(text)
    freq = {}
    for phrase in blob.noun_phrases:
        freq[phrase] = freq.get(phrase, 0) + 1

    scored_sentences = []
    for sent in blob.sentences:
        score = sum(freq.get(word.lower(), 0) for word in sent.words)
        scored_sentences.append((score, str(sent)))

    top_sentences = sorted(scored_sentences, reverse=True)[:3]
    return jsonify([sent for _, sent in top_sentences])

if __name__ == '__main__':
    app.run(debug=True)