# Arquivo que conterá todas as rotas da aplicação. Usamos o comando flask routes
from flask_restful import Api
from app.resources import auth


def init_app(app):
    # O preixo será utilizado em todas as rotas da aplicação
    api = Api(app, prefix="/api")
    api.add_resource(auth.Login, "/auth/login")
