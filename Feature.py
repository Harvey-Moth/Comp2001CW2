# app.py
from flask import abort, make_response, request
from config import db
from models import Feature, Fschema, Featureschemas, TrailFeature


def getall():
    Features = Feature.query.all()
    return Featureschemas.dump(Features)


def getone(id):
    feature = Feature.query.filter(Feature.FeatureID == id).one_or_none()
    if feature is not None:
        return Fschema.dump(feature)
    else:
        abort(404, f"Feature not found for Id: {id}")

def create(feature):
    
    newfeature = Fschema.load(feature, session=db.session)
    db.session.add(newfeature)
    db.session.commit()
    return Fschema.dump(newfeature)

def update(id, feature):
    updatefeature = Feature.query.filter(Feature.FeatureID == id).one_or_none()
    if updatefeature is not None:
        update = Fschema.load(feature, session=db.session)
        update.FeatureID = updatefeature.FeatureID 
        db.session.merge(update)
        db.session.commit()
        return Fschema.dump(updatefeature)
    else:
        abort(404, f"Feature not found for Id: {id}")

def delete(id): 
    feature = Feature.query.filter(Feature.FeatureID == id).one_or_none()
    featuresearch = TrailFeature.query.filter(TrailFeature.TrailFeatureID == id).all()
    if featuresearch is not None:
        for feature in featuresearch:
            db.session.delete(feature)
            db.session.commit()
    if feature is not None:
        db.session.delete(feature)
        db.session.commit()
        return make_response(f"Feature {id} deleted", 200)
    else:
        abort(404, f"Feature not found for Id: {id}")

