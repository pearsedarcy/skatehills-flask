from skatehills import db


class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"Event('{self.title}', '{self.date}', '{self.time}', '{self.location}', '{self.description}', '{self.image}')"


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    events = db.relationship("Event", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
