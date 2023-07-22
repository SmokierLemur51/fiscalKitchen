from datetime import datetime
from in_stock import db, login_manager
from flask_login import UserMixin

'''
	Database Tables Needed
		
		- User
		- Items/Ingredients
			- Separate Table for Kroger API?
		- Grocery List
		- Pantry
		- Recipies
		- Meals
		- Posts
		- Comments
		- Purchases
		- Expense Analysis Tracking
		- Budget
		- Paycheck
		- Cashapp/Venmo

'''

@login_manager.user_loader
def load_user(user_id):
	return User.quey.get(int(user_id))


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), nullable=False, unique=True)
	email = db.Column(db.String(120), nullable=False, unique=True)
	password = db.Column(db.String(60), nullable=False)


class 