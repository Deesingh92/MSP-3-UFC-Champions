from flask import render_template, request
from ufc import app, db
from ufc.models import WeightClass, Champion


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
            champions_filtered = [champion for champion in champions if champion['weight_class'] == weight_class]

        return render_template('fighters.html', champions=champions_filtered)

    return render_template('fighters.html', champions=None)