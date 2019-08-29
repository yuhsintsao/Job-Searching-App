from common.database import Database
from common.utils import Utils
import models.auth.errorhandler as ErrorHandlers

class Auth(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def _format2json(self):
        return {
            "username":self.username, 
            "password":self.password, 
        }

    def _save2db(self):
        Database.insert_one(collection="user", data=self._format2json())
 
    @classmethod
    def login(cls, username, password):
        login_info = Database.find_one(collection="user", query={ "username": username })
        if login_info and not Utils.verify_hashed_passord(password, login_info['password']):
            raise ErrorHandlers.InvalidInfo('Login fails! Please check your password.')
        elif login_info and Utils.verify_hashed_passord(password, login_info['password']):
            return True
        else:
            raise ErrorHandlers.UserNotFound('Please register first.')
            
    @classmethod
    def register(cls, username, password):
        user = Database.find_one(collection="user", query={ "username": username })
        if not username or not password:
            raise ErrorHandlers.InvalidInfo('Register fails! Please check your username and password.')
        elif user:
            raise ErrorHandlers.UserAlreadyExists('You have already registered. Welcome back! Please log in.')
        else:
            cls(username, Utils.hash_passord(password))._save2db()
            return True




        


     