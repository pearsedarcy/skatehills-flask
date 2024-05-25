from flask import render_template, request, redirect, url_for
from skatehills import app, db
from skatehills.models import Event, Hill


# Index Route
@app.route("/")
def index():
    """
    Renders the index.html template.

    Returns:
        The rendered index.html template.
    """
    return render_template("index.html")


# Hill Routes
@app.route("/hills", methods=["GET", "POST"])
def hills():
    """
    Renders the hills.html template and handles GET and POST requests.

    Returns:
        The rendered hills.html template with the hills data.
    """
    hills = Hill.query.order_by(Hill.name).all()
    return render_template("hills.html", hills=hills)


@app.route("/add_hills", methods=["GET", "POST"])
def add_hills():
    """
    Renders the add_hills.html template and handles GET and POST requests.

    Returns:
        - If the request method is POST, redirects to the hills route.
        - If the request method is GET, renders the add_hills.html template.
    """
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


@app.route("/edit_hill/<int:id>", methods=["GET", "POST"])
def edit_hill(id):
    """
    Renders the edit_hill.html template and handles GET and POST requests.

    Args:
        id (int): The ID of the hill to edit.

    Returns:
        - If the request method is POST, updates the hill data and redirects to the hills route.
        - If the request method is GET, renders the edit_hill.html template with the hill data.
    """
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


@app.route("/delete_hill/<int:id>", methods=["GET", "POST"])
def delete_hill(id):
    """
    Deletes a hill from the database.

    Args:
        id (int): The ID of the hill to delete.

    Returns:
        Redirects to the hills route.
    """
    hill = Hill.query.get_or_404(id)
    db.session.delete(hill)
    db.session.commit()
    return redirect(url_for("hills"))


# EVENTS ROUTES
@app.route("/events")
def events():
    """
    Renders the events.html template.

    Returns:
        The rendered events.html template with the events data.
    """
    events = Event.query.all()
    return render_template("events.html", events=events)


@app.route("/add_event", methods=["GET", "POST"])
def add_event():
    """
    Renders the add_event.html template and handles GET and POST requests.

    Returns:
        - If the request method is POST, creates a new event and redirects to the events route.
        - If the request method is GET, renders the add_event.html template with the hills data.
    """
    hills = Hill.query.order_by(Hill.name).all()
    if request.method == "POST":
        title = request.form.get("title")
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        location = request.form.get("location")
        description = request.form.get("description")
        image = request.form.get("image")
        hill_id = request.form.get("hill_id")
        event = Event(
            title=title,
            start_date=start_date,
            end_date=end_date,
            location=location,
            description=description,
            image=image,
            hill_id=hill_id,
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("events"))

    return render_template("add_event.html", hills=hills)


@app.route("/edit_event/<int:id>", methods=["GET", "POST"])
def edit_event(id):
    """
    Renders the edit_event.html template and handles GET and POST requests.

    Args:
        id (int): The ID of the event to edit.

    Returns:
        - If the request method is POST, updates the event data and redirects to the events route.
        - If the request method is GET, renders the edit_event.html template with the event data and hills data.
    """
    event = Event.query.get_or_404(id)
    if request.method == "POST":
        event.title = request.form.get("title")
        event.start_date = request.form.get("start_date")
        event.end_date = request.form.get("end_date")
        event.location = request.form.get("location")
        event.description = request.form.get("description")
        event.image = request.form.get("image")
        event.hill_id = request.form.get("hill_id")
        db.session.commit()
        return redirect(url_for("events"))
    hills = Hill.query.order_by(Hill.name).all()
    return render_template("edit_event.html", event=event, hills=hills)


@app.route("/delete_event/<int:id>", methods=["GET", "POST"])
def delete_event(id):
    """
    Deletes an event from the database.

    Args:
        id (int): The ID of the event to delete.

    Returns:
        Redirects to the events route.
    """
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for("events"))
