# app.py
from flask import abort, make_response, request
from config import db
from models import User, Uschema, Userschemas, Trail, TrailFeature


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
    if id == 1:
        abort(404, f"Admin user cannot be deleted")
    user = User.query.filter(User.UserID == id).one_or_none()
    Trails = Trail.query.filter(Trail.OwnerID == id).all()
    if user is not None:
        if Trails is not None:
            for trail in Trails:
                trail.OwnerID = 1
                db.session.add(trail)
        db.session.commit()
        db.session.delete(user)
        db.session.commit()
        return make_response(f"User {id} deleted", 200)
    else:
        abort(404, f"User not found for Id: {id}")
            
