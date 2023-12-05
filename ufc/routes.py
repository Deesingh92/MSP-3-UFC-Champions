from flask import render_template, request,  url_for
from ufc import app
from datetime import datetime
from ufc.models import Champion

champions = [
    Champion(name="Jon Jones", country="USA", weight_class="Heavyweight", start_date=datetime(2023, 3, 24), end_date=datetime.now(), image_url=None),
    Champion(name="Alex Pereira", country="Brazil", weight_class="Light Heavyweight", start_date=datetime(2023, 11, 11), end_date=datetime.now(), image_url=None),
    Champion(name="Sean Strickland", country="USA", weight_class="Middleweight", start_date=datetime(2023, 9, 10), end_date=datetime.now(), image_url=None),
    Champion(name="Leon Edwards", country="England", weight_class="Welterweight", start_date=datetime(2022, 8, 20), end_date=datetime.now(), image_url=None),
    Champion(name="Islam Makhachev", country="Dagestan", weight_class="Lightweight", start_date=datetime(2022, 10, 22), end_date=datetime.now(), image_url=None),
    Champion(name="Alexander Volkanovski", country="Australia", weight_class="Featherweight", start_date=datetime(2019, 12, 14), end_date=datetime.now(), image_url=None),
    Champion(name="Sean O'Malley", country="USA", weight_class="Bantamweight", start_date=datetime(2023, 8, 19), end_date=datetime.now(), image_url=None),
    Champion(name="Alex Pantoja", country="Brazil", weight_class="Flyweight", start_date=datetime(2023, 11, 14), end_date=datetime.now(), image_url=None),
]


@app.route("/")
def home():
    return render_template("base.html")

@app.route('/fighters', methods=['GET', 'POST'])
def fighters():
    if request.method == 'POST':
        weight_class = request.form.get('weight_class')
        if weight_class == 'all':
            champions_filtered = champions
        else:
            champions_filtered = [champion for champion in champions if champion.weight_class == weight_class]

        return render_template('fighters.html', champions=champions_filtered)

   
    for champion in champions:
        champion.image_url = url_for('static', filename='images/jon-jones.jpeg')
        print(champion.image_url)

    return render_template('fighters.html', champions=champions)
