from flask import Blueprint, render_template
from . import db
from .models import Votes, Voters

main = Blueprint('main', __name__)

@main.route('/')
def index():
    db.session.begin()
    votes = db.session.query(
        Votes
    ).all()
    all_vote = []
    for vote in votes:
        data = {
            'id': vote.id,
            'name': vote.name,
            'vote': vote.vote
        }
        all_vote.append(data)
    db.session.close()
    return render_template('main.html', all_vote=all_vote)

@main.route('/winner/<id>')
def winner(id):
    db.session.begin()
    winners = db.session.query(
        Voters
    ).filter(
        Voters.selection == id
    ).all()
    winners = [i.name for i in winners]
    db.session.close()
    return render_template('winner.html', winners=winners)