from sqlalchemy import func
from DB.models import Message
from app import db

class messageHandler():
    def createMessageDB(message_data):
        new_message = Message(
                id = messageHandler.generateId(),
                user_id = message_data['user_id'],
                repeat = message_data['repeat'],
                dest_groups_id = message_data['dest_groups_id'],
                time_to_send = message_data['time_to_send'],
                message_data = message_data['message_data'],
                message_title = message_data['message_title'])
    
        db.session.add(new_message)
        db.session.commit()
        return new_message

    @staticmethod
    def generateId():
        max_id = db.session.query(func.max(Message.id)).scalar()
        next_id = (max_id or 0) + 1
        return next_id

    def getMessageDB(message_id):
        message_to_return = Message.query.filter_by(id=message_id).first()
        if message_to_return:
            return message_to_return
        else:
            return "message not found"
    

    def updateMessageDB(message_data, message_id):
        message_to_update = Message.query.filter_by(id=message_id).first()
        if message_to_update:
            message_to_update.user_id = message_data['user_id']
            message_to_update.repeat = message_data['repeat']
            message_to_update.dest_groups_id = message_data['dest_groups_id']
            message_to_update.message_data = message_data['message_data']
            message_to_update.message_title = message_data['message_title']
            db.session.commit()
            return message_to_update
        else:
            return "message not found"
    

    def deleteMessageDB(message_id):
        message_to_delete = Message.query.filter_by(id=message_id).first()
        if message_to_delete:
            db.session.delete(message_to_delete)
            db.session.commit()
            return message_to_delete
        else:
            return "message not found"