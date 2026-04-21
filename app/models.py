from . import db
from datetime import datetime

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.String(50), nullable=False)
    restaurant_name = db.Column(db.String(120), nullable=False)
    restaurant_contact = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Available')
    ngo_name = db.Column(db.String(120), nullable=True)
    receiver_name = db.Column(db.String(120), nullable=True)
    receiver_phone = db.Column(db.String(120), nullable=True)

class FundDonor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    contact_info = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 stars
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    read = db.Column(db.Boolean, default=False)