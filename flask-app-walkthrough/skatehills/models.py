from skatehills import db


class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    start_date = db.Column(db.String, nullable=False)
    end_date = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    image = db.Column(db.String, nullable=False)
    hill_id = db.Column(db.Integer, db.ForeignKey("hill.id"))

    def __repr__(self):
        return f"Event('{self.title}', '{self.start_date}', '{self.end_date}', '{self.location}', '{self.description}', '{self.image}', '{self.hill_id}')"


class Hill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    start_location = db.Column(db.String, nullable=False)
    end_location = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    events = db.relationship("Event", backref="hill", lazy=True)

    def __repr__(self):
        return f"Hill('{self.name}', '{self.start_location}', '{self.end_location}', '{self.country}' ,  '{self.image}')"


# class User(db.Model):

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False)
#     password = db.Column(db.String, nullable=False)
#     events = db.relationship("Event", backref="author", lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"
