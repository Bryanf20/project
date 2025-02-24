from . import db

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    members = db.relationship('GroupMember', backref='group', lazy='dynamic', cascade='all, delete-orphan')
    resources = db.relationship('Resource', back_populates='group', cascade='all, delete-orphan')
    # messages = db.relationship('Message', backref='group', lazy='dynamic')
    # threads = db.relationship('Thread', backref='group', lazy='dynamic') 

    def __repr__(self):
        return f'<Group {self.name}>'
    

class GroupMember(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    joined_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<GroupMember user_id={self.user_id} group_id={self.group_id}>'
    
    
class GroupInvite(db.Model):
    __tablename__ = 'group_invites'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)  # Group FK
    email = db.Column(db.String(120), nullable=False)  # Email of the invitee
    invite_code = db.Column(db.String(36), unique=True, nullable=False)  # UUID for the invite
    invited_at = db.Column(db.DateTime, server_default=db.func.now())
    accepted = db.Column(db.Boolean, default=False)

