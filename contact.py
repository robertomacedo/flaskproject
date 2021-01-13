from flask import Blueprint, render_template


bp = Blueprint('contatct', __name__, url_prefix='/contact')

@bp.route('/', method=['GET', 'POST']) # Inserir GET e POST reconhece o form e seu get or post
def contact():
    return render_template('contact.html')

def configure(app):
    app.register_blueprint(bp)