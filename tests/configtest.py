# Create a test client using the Flask application configured for testing
import pytest
from config import config
from api.app import db
from api.routes import app
from api.models import Call


@pytest.fixture
def client():
    app.config.from_object(config['test'])
    with app.test_client() as client:
        with app.app_context():
            yield client


@pytest.fixture()
def init_database():
    db.create_all()

    # List of test users
    test_calls = [
        Call("user", 3000),
        Call("user", 31000)
    ]

    t_calls = list(test_calls)

    # Add the users to the database - add_all() is used to add multiple records
    db.session.add_all(t_calls)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!
    db.session.remove()  # looks like db.session.close() would work as well
    # Drop the database table
    db.drop_all()