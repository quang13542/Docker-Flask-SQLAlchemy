from flask.cli import FlaskGroup

from flask_project import *

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    try:
        db.session.add(Author(email="me@mail"))
        db.session.commit()
    except:
        print("exist")

if __name__ == "__main__":
    cli()