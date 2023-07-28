import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from prompts.investmentinfo import investmentprompt

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        investment_type = request.form["investment_type"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=investmentprompt(investment_type),
            temperature=0.6,
            max_tokens=100,
        )
        return redirect(url_for("index", result=response.choices[0].text.strip()))

    result = request.args.get("result")
    return render_template("index.html", result=result)

