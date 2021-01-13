from flask import Blueprint, render_template, request


bp = Blueprint('contatct', __name__, url_prefix='/contact')

@bp.route('/', methods=['GET', 'POST']) # Inserir GET e POST reconhece o form e seu get or post
def contact():
    if request.method == 'GET':
        return render_template('contact.html')

    # processa os dados do form
    print(request.form)
    return "Mensagem enviada com sucesso!"

def configure(app):
    app.register_blueprint(bp)