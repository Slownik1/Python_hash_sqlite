from dbConnection import *
import hashlib, uuid

password = input('Enter password: ')
if password!='':
    passwordRepeat = input('Repeat password: ')
    if password == passwordRepeat:
        salt = uuid.uuid4().hex
        hashedPassword = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100)
        dbInsert(hashedPassword, salt)
        print('OK !')
    else:
        print('password is not equals !')
else:
    print('Password can not be empty !')