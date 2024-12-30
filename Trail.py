# app.py
from flask import abort, make_response, request
from config import db
from models import Trail, Tschema, Trailschemas


def getall():
    Trails = Trail.query.all()
    return Trailschemas.dump(Trails)


def getone(id):
    trail = Trail.query.filter(Trail.TrailID == id).one_or_none()
    if trail is not None:
        return Tschema.dump(trail)
    else:
        abort(404, f"Trail not found for Id: {id}")

def create(trail):
    
    newtrail = Tschema.load(trail, session=db.session)
    db.session.add(newtrail)
    db.session.commit()
    return Tschema.dump(newtrail)

def update(id, trail):
    updatetrail = Trail.query.filter(Trail.TrailID == id).one_or_none()
    if updatetrail is not None:
        update = Tschema.load(trail, session=db.session)
        update.TrailID = updatetrail.TrailID 
        db.session.merge(update)
        db.session.commit()
        return Tschema.dump(updatetrail)
    else:
        abort(404, f"Trail not found for Id: {id}")

def delete(id): 
    trail = Trail.query.filter(Trail.TrailID == id).one_or_none()
    if trail is not None:
        db.session.delete(trail)
        db.session.commit()
        return make_response(f"Trail {id} deleted", 200)
    else:
        abort(404, f"Trail not found for Id: {id}")
