from flask import Flask, request, jsonify

app = Flask(__name__)

knowledge = {}

file = open("../dataset/knowledge.txt","r",encoding="utf-8")

for line in file:
    if "|" in line:
        q,a = line.split("|")
        knowledge[q.strip()] = a.strip()

@app.route("/ask",methods=["POST"])
def ask():
    data = request.json
    question = data["question"].lower()

    for q in knowledge:
        if q in question:
            return jsonify({"answer":knowledge[q]})

    return jsonify({"answer":"I don't know yet"})

app.run(host="0.0.0.0", port=5000)