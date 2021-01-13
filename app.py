import views
import contact
from flask import Flask


def create_app():
    app = Flask(__name__)
    views.configure(app)
    # configure extencions
    contact.configure(app)
    # congigure variables
    return app


