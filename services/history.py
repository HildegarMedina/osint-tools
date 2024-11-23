from domain.models import History as HistoryModel
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class History:

    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_list(self):
        history = self.db.session.query(HistoryModel).order_by(HistoryModel.created_at.desc()).all()
        return history

    def save(self, history):
        try:
            history = HistoryModel(
                tool=history["tool"],
                input=history["input"],
                created_at=datetime.now()
            )
            self.db.session.add(history)
            self.db.session.commit()
        except Exception as e:
            print(e)
            return False
