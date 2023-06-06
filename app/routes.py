from flask import request, jsonify, make_response
from DB.db_handler import messageHandler
from app import app
from DB.db_errors import *


@app.route("/message", methods=['POST'])
def createMessage():
    try:
        message_data = request.get_json()
        new_message = messageHandler.createMessageDB(message_data)
        return make_response(jsonify({'created message': new_message.json()}), 201)
    except Exception as e:
        error_message = DbErrors.handle_error(e)
        return make_response(jsonify({'error': error_message}), 500)


@app.route("/message/<id>", methods=['GET', 'PUT', 'DELETE'])
def handleMessage(id):
    if request.method == 'GET':
        return handleData.handle_get(id)


    elif request.method == 'PUT':
        return handleData.handle_put(id)


    elif request.method == 'DELETE':
        return handleData.handle_delete(id)


class handleData():
    def handle_get(id):
        try:
            message_to_return = messageHandler.getMessageDB(id)
            if message_to_return != "message not found":
                return make_response(jsonify({'message': message_to_return.json()}), 200)
            else:
                return make_response(jsonify({'error': 'Message not found'}), 404)
        except Exception as e:
            error_message = DbErrors.handle_error(e)
            return make_response(jsonify({'error': error_message}), 500)
        
    def handle_put(id):
        try:
            message_data = request.get_json()
            updated_message = messageHandler.updateMessageDB(message_data, id)
            if updated_message != "message not found":
                return make_response(jsonify({'message updated': updated_message.json()}), 200)
            else:
                return make_response(jsonify({'error': 'Message not found'}), 404)
        except Exception as e:
            error_message = DbErrors.handle_error(e)
            return make_response(jsonify({'error': error_message}), 500)
        
    def handle_delete(id):
        try:
            deleted_message = messageHandler.deleteMessageDB(id)
            if deleted_message != "message not found":
                return make_response(jsonify({'message deleted': deleted_message.json()}), 204)
            else:
                return make_response(jsonify({'error': 'Message not found'}), 404)
        except Exception as e:
            error_message = DbErrors.handle_error(e)
            return make_response(jsonify({'error': error_message}), 500)