from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email

class RestaurantFoodForm(FlaskForm):
    restaurant_name = StringField('Restaurant Name', validators=[DataRequired(), Length(max=120)])
    contact_number = StringField('Contact Number', validators=[DataRequired(), Length(max=120)])
    food_name = StringField('Food Name', validators=[DataRequired(), Length(max=120)])
    quantity = StringField('Quantity', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Add Food')

class RestaurantRegisterForm(FlaskForm):
    restaurant_id = StringField('Restaurant ID', validators=[DataRequired(), Length(max=120)])
    restaurant_name = StringField('Restaurant Name', validators=[DataRequired(), Length(max=120)])
    contact_number = StringField('Contact Number', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Register & Continue')

class NGOReceiveForm(FlaskForm):
    ngo_name = StringField('NGO Name', validators=[DataRequired(), Length(max=120)])
    receiver_name = StringField('Receiver Name', validators=[DataRequired(), Length(max=120)])
    receiver_phone = StringField('Receiver Phone', validators=[DataRequired(), Length(max=120)])
    food_item_id = SelectField('Choose Food Item', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Mark Received')

class NGORegisterForm(FlaskForm):
    ngo_id = StringField('NGO ID', validators=[DataRequired(), Length(max=120)])
    ngo_name = StringField('NGO Name', validators=[DataRequired(), Length(max=120)])
    contact_info = StringField('Contact Number', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Register & Continue')

class FundDonorForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(max=120)])
    contact_info = StringField('Contact Number', validators=[DataRequired(), Length(max=120)])
    email = StringField('Email', validators=[DataRequired(), Length(max=120)])
    amount = StringField('Amount', validators=[DataRequired(), Length(max=50)])
    submit = SubmitField('Submit Donation')

class DonorRegisterForm(FlaskForm):
    donor_id = StringField('Donor ID', validators=[DataRequired(), Length(max=120)])
    name = StringField('Full Name', validators=[DataRequired(), Length(max=120)])
    contact_info = StringField('Contact Number', validators=[DataRequired(), Length(max=120)])
    submit = SubmitField('Register & Continue')

class FeedbackForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired(), Length(min=2, max=120)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(max=120)])
    rating = SelectField('Rating', choices=[(i, f'{i} Star{"s" if i != 1 else ""}') for i in range(1, 6)], coerce=int, validators=[DataRequired()])
    message = TextAreaField('Feedback Message', validators=[DataRequired(), Length(min=10, max=1000)])
    submit = SubmitField('Submit Feedback')