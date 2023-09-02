from app import db, app
from models.models import Investment, Budget, Spending

def seed_data():


    with app.app_context():
        # Create Investment seed data
        investment1 = Investment(type='Bonds', information='Long term, low risk')
        investment2 = Investment(type='Stocks', information='Medium term, high risk')
        
        db.session.add(investment1)
        db.session.add(investment2)

        # Create Budget seed data
        budget1 = Budget(income=5000.0, rent=1000.0, utilities=200.0, groceries=300.0, others=500.0, plan='Plan A')
        budget2 = Budget(income=4000.0, rent=800.0, utilities=150.0, groceries=250.0, others=400.0, plan='Plan B')
        
        db.session.add(budget1)
        db.session.add(budget2)

        # Create Spending seed data
        spending1 = Spending(food=500.0, entertainment=200.0, transportation=100.0, others=150.0, analysis='Good')
        spending2 = Spending(food=400.0, entertainment=100.0, transportation=80.0, others=120.0, analysis='Fair')

        db.session.add(spending1)
        db.session.add(spending2)

        db.session.commit()

if __name__ == "__main__":
    seed_data()
