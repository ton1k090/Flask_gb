from wsgi import app
from blog.app import db


@app.cli.commands('init-db')
def init_db():
    db.create_all()