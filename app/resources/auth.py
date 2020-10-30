import logging

from flask_restful import Resource, reqparse
from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class Login(Resource):
    def get(self):
        return "Pagina de login"


class Register(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("email", required=True, help="O email deve ser obrigatório")
        parser.add_argument(
            "password", required=True, help="Senha deve ser obrigatório"
        )
        args = parser.parse_args()

        user = User.query.filter_by(email=args.email).first()

        if user:
            return {"error": "Email já registrado"}, 400

        user = User()
        user.email = args.email
        user.password = generate_password_hash(args.password, salt_length=10)

        db.session.add(user)

        try:
            db.session.commit()
            return {"message": "Usuário cadastrado com sucesso!"}, 201

        except Exception as ex:
            db.session.rollback()
            logging.critical(str(ex))
            return {"error": "Não foi possível registrar o usuário"}, 500
