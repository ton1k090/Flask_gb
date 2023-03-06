from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

login_manager = LoginManager()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '97rvg1t2+jd#i%wz(fz%yn-#27a#hb&aq5+)a@+n(8_$zz2=31'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))


    from .models import User

    register_blueprints(app)
    return app


def register_blueprints(app) -> Flask:
    from blog.user.views import user
    from blog.report.views import report
    from blog.auth.views import auth

    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(auth)



