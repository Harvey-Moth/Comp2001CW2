# app.py
from flask import abort, make_response, request
import requests
from config import db
from models import User, Uschema, Userschemas, Trail



def Authenticate():

    auth_url = 'https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users'
    userdetails = request.get_json()



    credentials = { 'Email': userdetails ["Email"], 'Password': userdetails["Password"]}

    response = requests.post(auth_url, json=credentials)

    if response.status_code == 200:
        try:
            if response.json() == ["Verified", "True"]:
                return make_response(f"Authenticated successfully:")
            else:
                return make_response(f"User does not exist")
        except requests.JSONDecodeError:
            return make_response(f"Response is not valid JSON. Raw response content:")
    else:
        return make_response(f"Authentication failed with status code {response.status_code}")
    






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
            
