import os 

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'voting.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

