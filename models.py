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
    ElevationGain = db.Column(db.Integer, nullable=False)
    RouteType = db.Column(db.String(500), nullable=False)
    OwnerID = db.Column(db.integer, db.ForeignKey('CW2.User.UserID'),nullable=False)
    Pt1_Lat = db.Column(db.Float, nullable=False)
    Pt1_Long = db.Column(db.Float, nullable=False)
    Pt1_Desc = db.Column(db.String(500), nullable=False)
    Pt2_lat = db.Column(db.Float, nullable=False)
    Pt2_long = db.Column(db.Float, nullable=False)
    Pt2_Desc = db.Column(db.String(500), nullable=False)
    User = db.relationship('User', backref='Trail', lazy=True)

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
    
    @validates('Pt1_Desc')
    def validate_Pt1_Desc(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid Description')
        return value
    
    @validates('Pt2_Desc')
    def validate_Pt2_Desc(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid Description')
        return value
    
    @validates('TrailName')
    def validate_TrailName(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid Trail Name')
        return value
    
    @validates('TrailDescription')
    def validate_TrailDescription(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid Trail Description')
        return value
    
    @validates('TrailSummary')
    def validate_TrailSummary(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid Trail Summary')
        return value
    
    @validates('Location')
    def validate_Location(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid Location')
        return value
    
    
class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        include_fk = True

    




class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'schema': 'CW2'}
    UserID = db.Column(db.Integer, autoincrement = True, primary_key=True)
    Username = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Role = db.Column(db.String(50), nullable=False)
    Trails = db.relationship('Trail', backref='User', lazy=True)

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

class Feature(db.Model):
    __tablename__ = 'Feature'
    __table_args__ = {'schema': 'CW2'}
    FeatureID = db.Column(db.Integer, autoincrement = True, primary_key=True)
    FeatureName = db.Column(db.String(50), nullable=False)
    Trail_Features = db.relationship('Trail_Feature', backref='Feature', lazy=True)

    @validates('FeatureName')
    def validate_FeatureName(self, value):
        if len(value) < 1:
            raise ValidationError('Invalid Feature Name')
        return value
    
class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        include_fk = True



class Trail_Feature (db.Model):
    __tablename__ = 'Trail_Feature'
    __table_args__ = {'schema': 'CW2'}
    TrailID = db.Column(db.Integer, db.ForeignKey('Trail.TrailID'), primary_key=True)
    Trail_FeatureID = db.Column(db.Integer, db.ForeignKey('CW2.Feature.FeatureID'), primary_key=True)
    Feature = db.relationship('Feature', backref='Trail_Feature', lazy=True)
    
class Trail_FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail_Feature
        include_fk = True


