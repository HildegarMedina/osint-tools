from domain.models import Log as LogModel
from datetime import datetime
class Log:

    def __init__(self, db):
        self.db = db

    def save(self, log):
        try:
            log = LogModel(
                tool=log["tool"],
                input=log["input"],
                created_at=datetime.now()
            )
            self.db.session.add(log)
            self.db.session.commit()
        except Exception as e:
            print(e)
            return False
