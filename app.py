import os
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import openai

from forms.forms import InvestmentForm, BudgetForm, SpendingForm
from prompts.investmentinfo import investmentprompt
from prompts.budgeting import budgetingprompt
from prompts.spending import spendingprompt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # replace with your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    form = InvestmentForm()
    if form.validate_on_submit():
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=investmentprompt(form.type.data),
            temperature=0.6,
            max_tokens=100,
        )
        return redirect(url_for("index", result=response.choices[0].text.strip()))

    result = request.args.get("result")
    return render_template("index.html", form=form, result=result) # pass the form to the template

@app.route("/budgeting", methods=("GET", "POST"))
def budgeting():
    form = BudgetForm()
    if form.validate_on_submit():
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=budgetingprompt(form.data),  # pass form data
            temperature=0.6,
            max_tokens=200,
        )
        return redirect(url_for("budgeting", result=response.choices[0].text.strip()))

    result = request.args.get("result")
    return render_template("budgeting.html", form=form, result=result)

@app.route("/spending", methods=("GET", "POST"))
def spending():
    form = SpendingForm()
    if form.validate_on_submit():
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=spendingprompt(form.data),  # pass form data
            temperature=0.6,
            max_tokens=200,
        )
        return redirect(url_for("spending", result=response.choices[0].text.strip()))

    result = request.args.get("result")
    return render_template("spending.html", form=form, result=result)
