from . import db

class Votes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    vote = db.Column(db.Integer)

    voters = db.relationship('Voters', backref='Votes', lazy='select')

class Voters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    selection = db.Column(db.Integer, db.ForeignKey('votes.id'))
