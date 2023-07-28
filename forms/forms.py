from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired


class InvestmentForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired()])
    information = StringField('Information', validators=[DataRequired()])
    submit = SubmitField('Submit')

class BudgetForm(FlaskForm):
    income = FloatField('Income', validators=[DataRequired()])
    rent = FloatField('Rent/Mortgage', validators=[DataRequired()])
    utilities = FloatField('Utilities', validators=[DataRequired()])
    groceries = FloatField('Groceries', validators=[DataRequired()])
    others = FloatField('Other Expenses', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SpendingForm(FlaskForm):
    food = FloatField('Food', validators=[DataRequired()])
    entertainment = FloatField('Entertainment', validators=[DataRequired()])
    transportation = FloatField('Transportation', validators=[DataRequired()])
    others = FloatField('Other Expenses', validators=[DataRequired()])
    submit = SubmitField('Submit')
