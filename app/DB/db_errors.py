from app import db


class DbErrors():
    def handle_error(error):
        db.session.rollback()
        error_message = str(error.orig)
        return error_message
    

