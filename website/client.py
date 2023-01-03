from flask import Blueprint, render_template, request, session, jsonify, redirect, url_for
from flask_socketio import emit
from . import db
from .models import Votes, Voters

client = Blueprint('client', __name__)

@client.route('/')
def index():
    if session.get('voted'):
        return redirect(url_for('client.finish'))
    client_id = session.get('client_id')
    db.session.begin()
    votes = db.session.query(
        Votes
    ).all()
    db.session.close()
    return render_template('client.html', votes=votes, client_id=client_id)

@client.route('/finish')
def finish():
    return render_template('finish.html')

@client.route('/clear')
def clear():
    session.clear()
    return redirect(url_for('client.index'))

@client.route('/join', methods=['POST'])
def join():
    db.session.begin()
    voter = Voters(name=request.json['name'], selection=None)
    db.session.add(voter)
    db.session.commit()
    session['client_id'] = voter.id
    db.session.close()
    return jsonify({
        'result': 'success'
    })

@client.route('/vote', methods=['POST'])
def vote():
    data = request.json

    db.session.begin()
    vote = db.session.query(
        Votes
    ).filter(
        Votes.id == data['id']
    ).first()
    if data['type'] == 'vote':
        vote.vote += 1
    else:
        vote.vote -= 1
    
    voter = db.session.query(
        Voters
    ).filter(
        Voters.id == session['client_id']
    ).first()
    voter.selection = data['id']
    session['voted'] = True
    db.session.commit()

    data = {
        'id': vote.id,
        'name': vote.name,
        'vote': vote.vote
    }
    db.session.close()

    emit('socketEvent', 
        data, 
        broadcast=True, 
        namespace='/'
    )
    return jsonify({
        'result': 'success'
    })
