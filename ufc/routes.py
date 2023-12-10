from flask import render_template, request,  url_for, session
from ufc import app
from datetime import datetime
from ufc.models import Champion

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
        champions_filtered = [champion for champion in champions if weight_class == 'all' or champion.weight_class == weight_class]

        return render_template('fighters.html', champions=champions_filtered)

    for champion in champions:
        champion.image_url = url_for('static', filename=f'images/{champion.name.lower().replace(" ", "-")}.jpeg')

    return render_template('fighters.html', champions=champions)

@app.route("/add_champion", methods=["GET", "POST"])
def add_champion():
    if request.method == "POST":
        champion = Champion(name=request.form.get("champion_name"))
        db.session.add(champion)
        db.session.commit()
        return redirect(url_for("fighters"))
    return render_template("add_champion.html")

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Simulate a simple user for demonstration purposes
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'demo' and password == 'password':
            session['user'] = username
            return redirect(url_for('home'))

        return render_template('signin.html', error='Invalid credentials' , champions=champions)

    return render_template('signin.html', error=None)