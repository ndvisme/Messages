from app import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    repeat = db.Column(db.String(80), nullable=False)
    dest_groups_id = db.Column(db.String(200), nullable=False)
    time_to_send = db.Column(db.String(120), nullable=False)
    message_data = db.Column(db.String(200), nullable=False)
    message_title = db.Column(db.String(80), nullable=False)