from app import db


class Machines(db.Model):
    """Machine record DB model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    os = db.Column(db.String(100), nullable=False)
    ip = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(100), nullable=False)


class Patches(db.Model):
    """Patch records DB model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    os = db.Column(db.String(100), nullable=False)


class Todo(db.Model):
    """to-do model"""
    # __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    description = db.Column(db.String(200), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    def __repr__(self):
        return '<Task %r>' % self.name
