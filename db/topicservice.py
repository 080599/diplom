from sqlalchemy.orm import Session
from db.models import Quiz

def create_topic(db: Session, topic: Quiz):
    db.add(topic)
    db.commit()
    db.refresh(topic)
    return topic



def get_all_topics(db: Session):
    return db.query(Quiz).all()


def delete_topic(db:Quiz):
    return db.query(Quiz).first()

