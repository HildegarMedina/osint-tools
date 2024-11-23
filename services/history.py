from domain.models import History as HistoryModel
from datetime import datetime

class History:

    def __init__(self, db):
        self.db = db

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
