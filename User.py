# app.py
from flask import abort, make_response, request
from config import db
from models import User, Uschema, Userschemas


def getall():
    users = User.query.all()
    return Userschemas.dump(users)


def getone(user_id):
    user = User.query.filter(User.user_id == user_id).one_or_none()
    if user is not None:
        return Uschema.dump(user)
    else:
        abort(404, f"User not found for Id: {user_id}")

def create(user):
    
    newuser = Uschema.load(user, session=db.session)
    db.session.add(newuser)
    db.session.commit()
    return Uschema.dump(newuser)

def update(user_id, user):
    updateuser = User.query.filter(User.user_id == user_id).one_or_none()
    if updateuser is not None:
        update = Uschema.load(user, session=db.session)
        update.user_id = updateuser.user_id
        db.session.merge(update)
        db.session.commit()
        return Uschema.dump(updateuser)
    else:
        abort(404, f"User not found for Id: {user_id}")

def delete(user_id): 
    user = User.query.filter(User.user_id == user_id).one_or_none()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {user_id} deleted", 200)
    else:
        abort(404, f"User not found for Id: {user_id}")
