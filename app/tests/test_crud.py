import pytest
from app import app, db
from DB.models import Message
from DB.db_handler import *


@pytest.fixture(scope="module")
def test_client():
    flask_app = app
    flask_app.config["TESTING"] = True

    with flask_app.test_client() as testing_message:
        with flask_app.app_context():
            create_test_messages()
            yield testing_message
            delete_test_messages("test")



    #### POSITIVE TESTS ####


def test_create_messages(test_client):
    message = {
        "user_id":"1",
        "repeat":"daily",
        "dest_groups_id":"1, 2, 3",
        "time_to_send":"2023-10-10, 10:10:10",
        "message_data":"test",
        "message_title":"test_create_message"}

    
    response = test_client.post('/message', json=message)
    delete_test_messages("test_create_message")
    assert response.status_code == 201
    

def test_get_message(test_client):
    create_test_messages()
    message = get_message_by_title("test")
    response = test_client.get(f'/message/{message.id}')
    assert response.status_code == 200


def test_update_message(test_client):
    new_message = {
        "user_id":"1",
        "repeat":"daily",
        "dest_groups_id":"1, 2, 3",
        "time_to_send":"2023-10-10, 10:10:10",
        "message_data":"test",
        "message_title":"test_update_message"}
    create_test_messages()
    message = get_message_by_title("test")
    response = test_client.put(f'/message/{message.id}', json=new_message)
    delete_test_messages("test_update_message")
    assert response.status_code == 200


def test_delete_message(test_client):
    create_test_messages()
    message = get_message_by_title("test")
    response = test_client.delete(f'/message/{message.id}')
    assert response.status_code == 204


   #### NEGATIVE TESTS ####

def test_get_non_existing_message(test_client):
    response = test_client.get('/message/-1')
    assert response.status_code == 404


def test_update_non_existing_message(test_client):
    response = test_client.put('/message/-1', json="")
    assert response.status_code == 404


def test_delete_non_existing_message(test_client):
    response = test_client.delete('/message/-1')
    assert response.status_code == 404


#####
def get_message_by_title(title):
    message = Message.query.filter_by(message_title=title).first()
    return message


def delete_test_messages(title):
    Message.query.filter_by(message_title=title).delete()
    db.session.commit()


def create_test_messages(user_id = "1",
                        repeat = "daily",
                        dest_groups_id = "1, 2, 3",
                        time_to_send = "2023-10-10, 10:10:10",
                        message_data = "test message body",
                        message_title = "test"):
    next_id = messageHandler.generateId()
    new_message = Message(  id = next_id, 
                            user_id = user_id,
                            repeat = repeat,
                            dest_groups_id = dest_groups_id,
                            time_to_send = time_to_send,
                            message_data = message_data,
                            message_title = message_title)
    db.session.add(new_message)
    db.session.commit()


        
