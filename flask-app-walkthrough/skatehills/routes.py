from flask import render_template, request, redirect, url_for

from skatehills import app, db

from skatehills.models import Event, Hill


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/events")
def events():
    events = Event.query.all()
    return render_template("events.html", events=events)


@app.route("/hills")
def hills():
    hills = Hill.query.order_by(Hill.name).all()
    return render_template("hills.html", hills=hills)


@app.route("/edit_hills/<int:id>", methods=["GET", "POST"])
def edit_hill(id):
    hill = Hill.query.get_or_404(id)
    if request.method == "POST":
        hill.name = request.form.get("name")
        hill.start_location = request.form.get("start_location")
        hill.end_location = request.form.get("end_location")
        hill.country = request.form.get("country")
        hill.image = request.form.get("image")
        db.session.commit()
        return redirect(url_for("hills"))
    return render_template("edit_hill.html", hill=hill)


@app.route("/add_hills", methods=["GET", "POST"])
def add_hills():
    if request.method == "POST":
        name = request.form.get("name")
        start_location = request.form.get("start_location")
        end_location = request.form.get("end_location")
        country = request.form.get("country")
        image = request.form.get("image")
        hill = Hill(
            name=name,
            start_location=start_location,
            end_location=end_location,
            country=country,
            image=image,
        )
        db.session.add(hill)
        db.session.commit()
        return redirect(url_for("hills"))
    return render_template("add_hills.html")
