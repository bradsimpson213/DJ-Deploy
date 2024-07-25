from .db import db, environment, SCHEMA, add_prefix_for_prod


class Joke(db.Model):
    __tablename__ = 'jokes'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key =True)
    joke_body = db.Column(db.String(255), nullable=False)
    punchline = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.String(50), default='G')
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))

    user = db.relationship("User", back_populates="joke")

    def to_dict(self):
        return {
            "id": self.id,
            "joke_body": self.joke_body,
            "punchline": self.punchline,
            "rating": self.rating,
            "user": self.user.to_dict_no_jokes()
        }

    def to_dict_no_user(self):
        return {
            "id": self.id,
            "joke_body": self.joke_body,
            "punchline": self.punchline,
            "rating": self.rating,
        }