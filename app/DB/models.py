from app import db


class Message(db.Model):
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    repeat = db.Column(db.String(100), nullable=True)
    dest_groups_id = db.Column(db.String(200), nullable=False)
    time_to_send = db.Column(db.DateTime(120), nullable=False)
    message_data = db.Column(db.String(500), nullable=False)
    message_title = db.Column(db.String(80), nullable=True)

    def json(self):
        return {'id': self.id, 
                'user_id': self.user_id,
                'repeat': self.repeat,
                'dest_groups_id': self.dest_groups_id, 
                'time_to_send': self.time_to_send,
                'message_data': self.message_data,
                'message_title': self.message_title}