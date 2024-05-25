from skatehills import db


class Event(db.Model):
    """
    Represents an event in the application.

    Attributes:
        id (int): The unique identifier of the event.
        title (str): The title of the event.
        start_date (str): The start date of the event.
        end_date (str): The end date of the event.
        location (str): The location of the event.
        description (str): The description of the event.
        image (str): The image URL of the event.
        hill_id (int): The foreign key referencing the associated hill.

    Relationships:
        hill (Hill): The associated hill object.
    """

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
    """
    Represents a hill in the application.

    Attributes:
        id (int): The unique identifier of the hill.
        name (str): The name of the hill.
        start_location (str): The starting location of the hill.
        end_location (str): The ending location of the hill.
        country (str): The country where the hill is located.
        image (str): The image URL of the hill.

    Relationships:
        events (List[Event]): The associated events of the hill.
    """

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
#     """
#     Represents a user in the application.

#     Attributes:
#         id (int): The unique identifier of the user.
#         username (str): The username of the user.
#         email (str): The email address of the user.
#         password (str): The password of the user.

#     Relationships:
#         events (List[Event]): The events created by the user.
#     """

#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False)
#     email = db.Column(db.String, nullable=False)
#     password = db.Column(db.String, nullable=False)
#     events = db.relationship("Event", backref="author", lazy=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"
