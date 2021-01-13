
def configure(app):

    @app.route('/')
    def index():
        return "<h1>Roberto Macedo Santos</h1>"

    @app.route('/api')
    def api():
        return 'Olá mundo'

    @app.route('/membro')
    def membro():
        return '<h1>Nome : Emily de Jesus</h1>'

