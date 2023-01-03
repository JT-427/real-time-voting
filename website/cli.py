from flask import Blueprint

from . import db
from .models import Votes

command = Blueprint('command', __name__, cli_group=None)

@command.cli.command('reset')
def reset():
    db.drop_all()
    db.create_all()
    db.session.begin()
    for i in ['哆啦Ａ夢', '哆啦Ｂ夢', '哆啦Ｃ夢', '哆啦Ｄ夢']:
        db.session.add(Votes(name=i, vote=0))
    db.session.commit()
    db.session.close()