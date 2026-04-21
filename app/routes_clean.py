from flask import render_template, redirect, url_for, request, session
from . import app, db
from .forms import RestaurantFoodForm, NGOReceiveForm, FundDonorForm, RestaurantRegisterForm, NGORegisterForm, DonorRegisterForm
from .models import FoodItem, FundDonor

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('login_choice.html')

@app.route('/register')
def register():
    return render_template('register_choice.html')

# Restaurant Routes
@app.route('/restaurant/register', methods=['GET', 'POST'])
def restaurant_register():
    form = RestaurantRegisterForm()
    if form.validate_on_submit():
        session['user_type'] = 'restaurant'
        session['restaurant_name'] = form.restaurant_name.data
        session['restaurant_id'] = form.restaurant_id.data
        return redirect(url_for('restaurant_dashboard'))
    return render_template('restaurant_register.html', form=form)

@app.route('/restaurant/login', methods=['GET', 'POST'])
def restaurant_login():
    if request.method == 'POST':
        session['user_type'] = 'restaurant'
        session['restaurant_id'] = request.form.get('restaurant_id')
        return redirect(url_for('restaurant_dashboard'))
    return render_template('restaurant_login.html')

@app.route('/restaurant/dashboard', methods=['GET', 'POST'])
def restaurant_dashboard():
    form = RestaurantFoodForm()
    items = FoodItem.query.order_by(FoodItem.id.desc()).all()
    if form.validate_on_submit():
        food = FoodItem(
            restaurant_name=form.restaurant_name.data,
            restaurant_contact=form.contact_number.data,
            food_name=form.food_name.data,
            quantity=form.quantity.data,
        )
        db.session.add(food)
        db.session.commit()
        return redirect(url_for('restaurant_dashboard'))
    return render_template('restaurant_dashboard.html', form=form, items=items)

# NGO Routes
@app.route('/ngo/register', methods=['GET', 'POST'])
def ngo_register():
    form = NGORegisterForm()
    if form.validate_on_submit():
        session['user_type'] = 'ngo'
        session['ngo_name'] = form.ngo_name.data
        session['ngo_id'] = form.ngo_id.data
        return redirect(url_for('ngo_dashboard'))
    return render_template('ngo_register.html', form=form)

@app.route('/ngo/login', methods=['GET', 'POST'])
def ngo_login():
    if request.method == 'POST':
        session['user_type'] = 'ngo'
        session['ngo_id'] = request.form.get('ngo_id')
        return redirect(url_for('ngo_dashboard'))
    return render_template('ngo_login.html')

@app.route('/ngo/dashboard', methods=['GET', 'POST'])
def ngo_dashboard():
    form = NGOReceiveForm()
    available_items = FoodItem.query.filter_by(status='Available').all()
    form.food_item_id.choices = [
        (item.id, f"{item.food_name} from {item.restaurant_name} ({item.quantity})")
        for item in available_items
    ] or [(0, 'No available items')]
    if form.validate_on_submit() and form.food_item_id.data != 0:
        item = FoodItem.query.get(form.food_item_id.data)
        if item:
            item.ngo_name = form.ngo_name.data
            item.receiver_name = form.receiver_name.data
            item.receiver_phone = form.receiver_phone.data
            item.status = 'Received'
            db.session.commit()
        return redirect(url_for('ngo_dashboard'))
    return render_template('ngo_dashboard.html', form=form, available_items=available_items)

# Fund Donor Routes
@app.route('/donor/register', methods=['GET', 'POST'])
def donor_register():
    form = DonorRegisterForm()
    if form.validate_on_submit():
        session['user_type'] = 'donor'
        session['donor_name'] = form.name.data
        session['donor_id'] = form.donor_id.data
        return redirect(url_for('donor_form'))
    return render_template('donor_register.html', form=form)

@app.route('/donor/login', methods=['GET', 'POST'])
def donor_login():
    if request.method == 'POST':
        session['user_type'] = 'donor'
        session['donor_id'] = request.form.get('donor_id')
        return redirect(url_for('donor_form'))
    return render_template('donor_login.html')

@app.route('/donor/donate', methods=['GET', 'POST'])
def donor_form():
    form = FundDonorForm()
    donors = FundDonor.query.order_by(FundDonor.id.desc()).all()
    if form.validate_on_submit():
        try:
            amount = float(form.amount.data)
        except ValueError:
            amount = 0.0
        donor = FundDonor(
            name=form.name.data,
            contact_info=form.contact_info.data,
            email=form.email.data,
            amount=amount,
        )
        db.session.add(donor)
        db.session.commit()
        return redirect(url_for('donor_form'))
    return render_template('donor_form.html', form=form, donors=donors)

# Admin Routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        session['user_type'] = 'admin'
        session['admin_id'] = request.form.get('admin_id')
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    donors = FundDonor.query.order_by(FundDonor.id.desc()).all()
    food_items = FoodItem.query.order_by(FoodItem.id.desc()).all()
    available_count = FoodItem.query.filter_by(status='Available').count()
    total_amount = sum(donor.amount for donor in donors)
    return render_template(
        'admin_dashboard.html',
        donors=donors,
        food_items=food_items,
        available_count=available_count,
        total_amount=total_amount,
    )

# Other Routes
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('landing'))

@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template('contact.html')
    return render_template('contact.html')
