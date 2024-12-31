# app.py
# app.py
from flask import abort, make_response, request
from config import db
from models import TrailFeature, TFschema, TrailFeatureschemas


def getall():
    trailfeatures = TrailFeature.query.all()
    return TrailFeatureschemas.dump(trailfeatures)


def getone(id):
    trailfeature = TrailFeature.query.filter(TrailFeature.TrailFeatureID == id).one_or_none() #Not really needed as is, would be better to check and get all the features attached to a given trail ID 
    if trailfeature is not None:
        return TFschema.dump(trailfeature)
    else:
        abort(404, f"TrailFeature not found for Id: {id}")

def create(trailfeature):
    
    newtrailfeature = TFschema.load(trailfeature, session=db.session)
    db.session.add(newtrailfeature)
    db.session.commit()
    return TFschema.dump(newtrailfeature)

# def update(id, trailfeature):
#     updatetrailfeature = TrailFeature.query.filter(TrailFeature.TrailFeatureID == id).one_or_none() 
#     if updatetrailfeature is not None:
#         update = TFschema.load(trailfeature, session=db.session)
#         update.TrailFeatureID = updatetrailfeature.TrailFeatureID 
#         db.session.merge(update)
#         db.session.commit()
#         return TFschema.dump(updatetrailfeature)
#     else:
#         abort(404, f"TrailFeature not found for Id: {id}")

def delete(id): 
    trailfeature = TrailFeature.query.filter(TrailFeature.TrailFeatureID == id).one_or_none()
    if trailfeature is not None:
        db.session.delete(trailfeature)
        db.session.commit()
        return make_response(f"TrailFeature {id} deleted", 200)
    else:
        abort(404, f"TrailFeature not found for Id: {id}") # This is not going to work, as is.
