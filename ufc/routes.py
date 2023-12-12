from flask import render_template, request, url_for, session, flash, redirect
from ufc import app, db
from datetime import datetime
from ufc.models import Champion, User
from flask_login import login_required, current_user, logout_user
from werkzeug.security import generate_password_hash

champions = [
    Champion(name="Jon Jones", country="USA", weight_class="Heavyweight", start_date=datetime(2023, 3, 24), end_date=datetime.now(), image_url="static/images/jon-jones.jpeg"),
    Champion(name="Alex Pereira", country="Brazil", weight_class="Light Heavyweight", start_date=datetime(2023, 11, 11), end_date=datetime.now(), image_url="static/images/alex-pereira.jpeg"),
    Champion(name="Sean Strickland", country="USA", weight_class="Middleweight", start_date=datetime(2023, 9, 10), end_date=datetime.now(), image_url="static/images/sean-strickland.jpeg"),
    Champion(name="Leon Edwards", country="England", weight_class="Welterweight", start_date=datetime(2022, 8, 20), end_date=datetime.now(), image_url="static/images/leon-edwards.jpeg"),
    Champion(name="Islam Makhachev", country="Dagestan", weight_class="Lightweight", start_date=datetime(2022, 10, 22), end_date=datetime.now(), image_url="static/images/islam-makhachev.jpeg"),
    Champion(name="Alexander Volkanovski", country="Australia", weight_class="Featherweight", start_date=datetime(2019, 12, 14), end_date=datetime.now(), image_url="static/images/alexander-volkanovski.jpeg"),
    Champion(name="Sean O'Malley", country="USA", weight_class="Bantamweight", start_date=datetime(2023, 8, 19), end_date=datetime.now(), image_url="static/images/sean-o'malley.jpeg"),
    Champion(name="Alex Pantoja", country="Brazil", weight_class="Flyweight", start_date=datetime(2023, 11, 14), end_date=datetime.now(), image_url="static/images/alex-pantoja.jpeg"),
]

@app.route("/")
def home():
    return render_template("base.html", champions=champions)

@app.route('/fighters', methods=['GET', 'POST'])
def fighters():
    if request.method == 'POST':
        weight_class = request.form.get('weight_class')
        champions_filtered = Champion.query.filter_by(weight_class=weight_class).all() if weight_class != 'all' else Champion.query.all()

        return render_template('fighters.html', champions=champions_filtered)

    champions = Champion.query.all()
    return render_template('fighters.html', champions=champions)


@app.route("/add_champion", methods=["GET", "POST"])
def add_champion():
    if request.method == "POST":
        name = request.form.get("champion_name")
        
        
        new_champion = Champion(
            name=name,
            country="",  
            weight_class="",
            start_date=datetime.now(),
            end_date=datetime.now(),
            image_url=""
        )
        
        db.session.add(new_champion)
        db.session.commit()
        
        # Now the new_champion object should have a valid id
        return redirect(url_for("fighters"))
    
    return render_template("add_champion.html")

@app.route("/edit_champion/<int:champion_id>", methods=["GET", "POST"])
@login_required
def edit_champion(champion_id):
    champion = Champion.query.get(champion_id)

    if not champion:
        return render_template("404.html"), 404

    if request.method == "POST":
        # Update champion details
        champion.name = request.form.get("name")
        champion.country = request.form.get("country")
        champion.weight_class = request.form.get("weight_class")
        champion.start_date = datetime.strptime(request.form.get("start_date"), "%Y-%m-%d")
        champion.end_date = datetime.strptime(request.form.get("end_date"), "%Y-%m-%d")
        champion.image_url = url_for('static', filename=f'images/{champion.name.lower().replace(" ", "-")}.jpeg')

        db.session.commit()
        return redirect(url_for("fighters"))

    return render_template("edit_champion.html", champion=champion)


@app.route('/delete_champion/<int:champion_id>', methods=['GET', 'POST'])
@login_required
def delete_champion(champion_id):
    champion = Champion.query.get_or_404(champion_id)

    if request.method == 'POST':
        db.session.delete(champion)
        db.session.commit()
        flash(f"Champion '{champion.name}' deleted successfully.", 'success')
        return redirect(url_for('fighters'))

    return render_template('confirm_delete_champion.html', champion=champion)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('fighters'))

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')

            # Redirect to add_champions after successful login
            return redirect(url_for('add_champion'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('signin.html')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if the username is already taken
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already exists. Please choose a different one.", "danger")
            return redirect(url_for("signup"))

        # Hash the password before storing it
        hashed_password = generate_password_hash(password, method="sha256")

        # Create a new user instance
        new_user = User(username=username, password=hashed_password)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully. You can now sign in.", "success")
        return redirect(url_for("signin"))

    return render_template("signup.html")   

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))   


if __name__ == '__main__':
    app.run(debug=True)