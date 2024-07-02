from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from main import app
import os

class Base(DeclarativeBase):
  pass

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(model_class=Base)
db.init_app(app)





