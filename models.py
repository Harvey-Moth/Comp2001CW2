# models.py
from marshmallow import fields, validates, ValidationError
from config import db, ma

class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'CW2'}
    UserID = db.Column(db.Integer, autoincrement = True, primary_key=True)
    Username = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Role = db.Column(db.String(50), nullable=False)
    @validates('Role')
    def validate_Role(self, value):
        if value not in ['Admin', 'User']:
            raise ValidationError('Invalid Role')
        return value
    
    @validates('Email')
    def validate_Email(self, value):
        if len(value) < []:
            raise ValidationError('Invalid Email')
        return value
    
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        load_instance = True
        sqla_session = db.session


Uschema = UserSchema()
Userschemas = UserSchema(many=True)





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
    ElevationGain = db.Column(db.Integer, nullable=False)
    RouteType = db.Column(db.String(500), nullable=False)
    OwnerID = db.Column(db.Integer, db.ForeignKey('CW2.User.UserID'),nullable=False)
    Pt1_Lat = db.Column(db.Float, nullable=False)
    Pt1_Long = db.Column(db.Float, nullable=False)
    Pt1_Desc = db.Column(db.String(500), nullable=False)
    Pt2_Lat = db.Column(db.Float, nullable=False)
    Pt2_Long = db.Column(db.Float, nullable=False)
    Pt2_Desc = db.Column(db.String(500), nullable=False)
    Pt3_Lat = db.Column(db.Float, nullable=True)
    Pt3_Long = db.Column(db.Float, nullable=True)
    Pt3_Desc = db.Column(db.String(500), nullable=True)
    Pt4_Lat = db.Column(db.Float, nullable=True)
    Pt4_Long = db.Column(db.Float, nullable=True)
    Pt4_Desc = db.Column(db.String(500), nullable=True)
    Pt5_Lat = db.Column(db.Float, nullable=True)
    Pt5_Long = db.Column(db.Float, nullable=True)
    Pt5_Desc = db.Column(db.String(500), nullable=True)
    User = db.relationship('User', backref='Trails')

    @validates('RouteType')
    def validate_RouteType(self, value):
        if value not in ['Loop', 'Out and Back', 'Point to Point']:
            raise ValidationError('Invalid Route Type')
        return value    

    @validates('Difficulty')
    def validate_Difficulty(self, value):
        if value not in ['Easy', 'Moderate', 'Hard']:
            raise ValidationError('Invalid Difficulty')
        return value
    
    @validates('Length')
    def validate_Length(self, value):
        if value < 0:
            raise ValidationError('Invalid Length')
        return value
    
    @validates('ElevationGain')
    def validate_ElevationGain(self, value):
        if value < 0:
            raise ValidationError('Invalid Elevation Gain')
        return value
    
    @validates('Pt1_Lat')
    def validate_Pt1_Lat(self, value):
        if value < -90 or value > 90:
            raise ValidationError('Invalid Latitude')
        return value
    
    @validates('Pt1_Long')
    def validate_Pt1_Long(self, value):
        if value < -180 or value > 180:
            raise ValidationError('Invalid Longitude')
        return value
    
    @validates('Pt2_Lat')
    def validate_Pt2_Lat(self, value):
        if value < -90 or value > 90:
            raise ValidationError('Invalid Latitude')
        return value
    
    @validates('Pt2_Long')
    def validate_Pt2_Long(self, value):
        if value < -180 or value > 180:
            raise ValidationError('Invalid Longitude')
        return value
    
    @validates('Pt3_Lat')
    def validate_Pt3_Lat(self, value):
        if value < -90 or value > 90:
            raise ValidationError('Invalid Latitude')
        return value
    
    @validates('Pt3_Long')
    def validate_Pt3_Long(self, value):
        if value < -180 or value > 180:
            raise ValidationError('Invalid Longitude')
        return value
    
    @validates('Pt4_Lat')
    def validate_Pt4_Lat(self, value):
        if value < -90 or value > 90:
            raise ValidationError('Invalid Latitude')
        return value
    
    @validates('Pt4_Long')
    def validate_Pt4_Long(self, value):
        if value < -180 or value > 180:
            raise ValidationError('Invalid Longitude')
        return value
    
    @validates('Pt5_Lat')
    def validate_Pt5_Lat(self, value):
        if value < -90 or value > 90:
            raise ValidationError('Invalid Latitude')
        return value
    
    @validates('Pt5_Long')
    def validate_Pt5_Long(self, value):
        if value < -180 or value > 180:
            raise ValidationError('Invalid Longitude')
        return value
    
    
class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        include_fk = True
        load_instance = True
        sqla_session = db.session

Tschema = TrailSchema()
Trailschemas = TrailSchema(many=True)



    




class Feature(db.Model):
    __tablename__ = 'Feature'
    __table_args__ = {'schema': 'CW2'}
    FeatureID = db.Column(db.Integer, autoincrement = True, primary_key=True)
    FeatureName = db.Column(db.String(50), nullable=False)

    
class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        include_fk = True
        load_instance = True
        sqla_session = db.session


Fschema = FeatureSchema()
Featureschemas = FeatureSchema(many=True)


class TrailFeature (db.Model):
    __tablename__ = 'TrailFeature'
    __table_args__ = {'schema': 'CW2'}
    TrailID = db.Column(db.Integer, db.ForeignKey('CW2.Trail.TrailID'), primary_key=True)
    TrailFeatureID = db.Column(db.Integer, db.ForeignKey('CW2.Feature.FeatureID'), primary_key=True)
    Feature = db.relationship('Feature', backref='TrailFeatures')
    Trail = db.relationship('Trail', backref='TrailFeatures')
    
class TrailFeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TrailFeature
        include_fk = True
        load_instance = True
        sqla_session = db.session

TFschema = TrailFeatureSchema()
TrailFeatureschemas = TrailFeatureSchema(many=True)
