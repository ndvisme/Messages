import pytest
from app import app, db
from DB.models import Message


@pytest.fixture(scope="module")
def test_client():
    flask_app = app
    flask_app.config["TESTING"] = True

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client
            # after the test is done, delete the test user record
            test_message = Message.query.filter_by(id="1234").first()
            if test_message:
                db.session.delete(test_message)
                db.session.commit()


def test_messages_db():
    with app.app_context():
        # create a test message
        test_message = Message(
            id = 1234,
            user_id = 5678,
            repeat = 'daily',
            dest_groups_id = '2, 3',
            time_to_send = '0113467',
            message_data = '''Hey team, don't forget - today's class starts at 8AM.''',
            message_title = 'Daily class reminder'
            )
        db.session.add(test_message)
        db.session.commit()

        # check if the user was saved in the db
        saved_message = Message.query.filter_by(id=1234).first()
        assert saved_message is not None