from flask import render_template, request, redirect, url_for

from skatehills import app, db

from skatehills.models import Event, User


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/events")
def events():
    events = Event.query.all()
    return render_template("events.html", events=events)
