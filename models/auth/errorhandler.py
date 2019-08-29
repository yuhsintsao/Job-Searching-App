class ErrorHandler(Exception):
    def __init__(self, message):
        self.message = message

class UserNotFound(ErrorHandler):
    pass

class UserAlreadyExists(ErrorHandler):
    pass

class InvalidInfo(ErrorHandler):
    pass