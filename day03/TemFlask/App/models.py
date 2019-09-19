from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# animal
#   name  color
#   cat   white
#   dog   black
#   hen   red


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(32))
    color = db.Column(db.String(32))

    __tablename__ = "animal1"
