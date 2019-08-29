from passlib.hash import pbkdf2_sha512
from dataclasses import dataclass

class Utils:

    @staticmethod
    def hash_passord(password:str) -> str:
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def verify_hashed_passord(password:str, hashed_password:str) -> bool:
        if pbkdf2_sha512.verify(password, hashed_password):
            return True
        return False


