from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(config)
# migrate = Migrate(app, db)

from app import routes, pdf_creator
