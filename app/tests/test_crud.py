import pytest
from app import app, db
from DB.models import Message


@pytest.fixture(scope="module")
def test_client():
    flask_app = app
    flask_app.config["TESTING"] = True

    with flask_app.test_client() as testing_message:
        with flask_app.app_context():
            create_test_messages()
            yield testing_message
            delete_test_messages("test")


def create_test_messages():
    message_1 = get_message_by_title("test")
    if message_1 is None:
        message_1 = Message(
                user_id = "1",
                repeat = "daily",
                dest_groups_id = "1, 2, 3",
                time_to_send = "2023-08-15, 10:10:10",
                message_data = "history is happening and we happen to be in the greatest city in the world",
                message_title = "test")
        
        db.session.add(message_1)
        
    message_2 = get_message_by_title("test")
    if message_2 is None:
        message_2 = Message(
                user_id = "1",
                repeat = "daily",
                dest_groups_id = "4, 5",
                time_to_send = "2023-12-15, 09:09:06",
                message_data = "rise up",
                message_title = "test")
    
        db.session.add(message_2)

    db.session.commit()



    #### POSITIVE TESTS ####


def test_create_messages(test_client):
    message_3 =  {
        "user_id":"1",
        "repeat":"weekly",
        "dest_groups_id":"13, 12",
        "time_to_send":"2023-09-15, 10:10:10",
        "message_data":"theres a million things I havent done but just you wait",
        "message_title":"test"}
    
    message_4 = {
        "user_id":"1",
        "repeat":"monthly",
        "dest_groups_id":"200, 1000",
        "time_to_send":"2024-09-15, 10:30:10",
        "message_data":"just you wait",
        "message_title":"test"}
    
    response = test_client.post('/message', json=message_3)
    assert response.status_code == 201

    response = test_client.post('/message', json=message_4)
    assert response.status_code == 201
    


def test_get_message(test_client):
    message = get_message_by_title("test")
    response = test_client.get(f'/message/{message.id}')
    assert response.status_code == 200


def test_update_message(test_client):
    new_message =  {
        "user_id" : "1",
        "repeat" : "daily",
        "dest_groups_id" : "1, 2, 3",
        "time_to_send" : "2023-08-15, 10:10:10",
        "message_data" : "history is happening and we happen to be in the greatest city in the world",
        "message_title" : "test"}
    message = get_message_by_title("test")
    response = test_client.put(f'/message/{message.id}', json=new_message)
    assert response.status_code == 200


def test_delete_message(test_client):
    message = get_message_by_title("test")
    response = test_client.delete(f'/message/{message.id}')
    assert response.status_code == 204


# #### NEGATIVE TESTS ####

def test_get_non_existing_message(test_client):
    response = test_client.get('/message/-1')
    assert response.status_code == 404


def test_update_non_existing_message(test_client):
    new_message =  {
                "user_id" : "1",
                "repeat" : "daily",
                "dest_groups_id" : "1, 2, 3",
                "time_to_send" : "2023-08-15, 10:10:10",
                "message_data" : "history is happening and we happen to be in the greatest city in the world",
                "message_title" : "test"}  
    response = test_client.put('/message/-1', json=new_message)
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



