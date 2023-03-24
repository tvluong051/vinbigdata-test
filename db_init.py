from api.app import create_app, db
from api.models import Call


def init_db():
	app = create_app()
	app.app_context().push()
	db.create_all()

init_db()