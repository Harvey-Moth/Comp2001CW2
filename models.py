# models.py
from marshmallow import fields, validates, ValidationError
from config import db, ma

class Trail(db.Model):
    __tablename__ = 'Trail'
    __table_args__ = {'schema': 'CW2'}
    TrailID = db.Column(db.Integer, autoincrement = True, primary_key=True)
    TrailName = db.Column(db.String(50), nullable=False)
    Length = db.Column(db.Float, nullable=False)
    Difficulty = db.Column(db.String(50), nullable=False)
    TrailDescription = db.Column(db.String(500), nullable=False)
    TrailSummary = db.Column(db.String(500), nullable=False)
    Location = db.Column(db.String(500), nullable=False)
    ElevationGain = db.Column(db.String(500), nullable=False)
    RouteType = db.Column(db.String(500), nullable=False)
    OwnerID = db.Column(db.String(500), db.ForeignKey('CW2.User.UserID'),nullable=False)
    Pt1_Lat = db.Column(db.String(500), nullable=False)
    Pt1_Long = db.Column(db.String(500), nullable=False)
    Pt1_Desc = db.Column(db.String(500), nullable=False)
    Pt2_lat = db.Column(db.String(500), nullable=False)
    Pt2_long = db.Column(db.String(500), nullable=False)
    Pt2_Desc = db.Column(db.String(500), nullable=False)
    User = db.relationship('User', backref='Trail', lazy=True)
    

class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'CW2'}
    UserID = db.Column(db.String(50), primary_key=True)
    Username = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Role = db.Column(db.String(50), nullable=False)
    Trails = db.relationship('Trail', backref='User', lazy=True)


class Feature(db.Model):
    __tablename__ = 'Feature'
    __table_args__ = {'schema': 'CW2'}
    FeatureID = db.Column(db.Integer, autoincrement = True, primary_key=True)
    FeatureName = db.Column(db.String(50), nullable=False)
    Trail_Features = db.relationship('Trail_Feature', backref='Feature', lazy=True)



class Trail_Feature (db.Model):
    __tablename__ = 'Trail_Feature'
    __table_args__ = {'schema': 'CW2'}
    TrailID = db.Column(db.Integer, db.ForeignKey('Trail.TrailID'), primary_key=True)
    Trail_FeatureID = db.Column(db.Integer, db.ForeignKey('CW2.Feature.FeatureID'), primary_key=True)
    Feature = db.relationship('Feature', backref='Trail_Feature', lazy=True)
    
