from flask import Flask
from flask import SQLAlchemy

# Inicjalizacja aplikacji Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///watches.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicjalizacja bazy danych SQLAlchemy
db = SQLAlchemy(app)

# Importowanie modułów routes i models
from app import routes, models
