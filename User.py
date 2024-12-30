# app.py
from flask import abort, make_response, request
from config import db
from models import User, Uschema, Userschemas


def getall():
    users = User.query.all()
    return Userschemas.dump(users)


def getone(id):
    user = User.query.filter(User.UserID == id).one_or_none()
    if user is not None:
        return Uschema.dump(user)
    else:
        abort(404, f"User not found for Id: {id}")

def create(user):
    
    newuser = Uschema.load(user, session=db.session)
    db.session.add(newuser)
    db.session.commit()
    return Uschema.dump(newuser)

def update(id, user):
    updateuser = User.query.filter(User.UserID == id).one_or_none()
    if updateuser is not None:
        update = Uschema.load(user, session=db.session)
        update.UserID = updateuser.UserID 
        db.session.merge(update)
        db.session.commit()
        return Uschema.dump(updateuser)
    else:
        abort(404, f"User not found for Id: {id}")

def delete(id): 
    user = User.query.filter(User.UserID == id).one_or_none()
    if user is not None:
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {id} deleted", 200)
    else:
        abort(404, f"User not found for Id: {id}")
