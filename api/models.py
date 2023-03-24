from api.app import db
from datetime import datetime

class Call(db.Model):
    __tablename__ = 'calls'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(32), index=True)
    call_duration = db.Column(db.Integer)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, user_name, call_duration):
        self.user_name = user_name
        self.call_duration = call_duration

    def __repr__(self):
        return f"'<Call: User={self.user_name}, Duration={self.call_duration} ms at {self.create_at}>"


class Billing:
    def __init__(self, call_count, block_count):
        self.call_count = call_count
        self.block_count = block_count


def save_call(call: Call):
    db.session.add(call)
    db.session.commit()