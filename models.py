from app import db
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin

"""
Command for DB
-----------------------
py manage.py db migrate
py manage.py db upgrade
db.session.add(p)
db.session.commit()
"""

def slugify(title):
    pattern = r'[^\w+]'
    return re.sub(pattern, '_', title).lower()

# Create table post_tags for united table post and tag as "many to many"
post_tags = db.Table('post_tegs',
                     db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                     )


class Post(db.Model):
    """Create Table Post with column id, title, slug, body, created date"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        """Create slug"""

        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'


class Tag(db.Model):
    """Create table Tag with column: id, name, slug"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(140))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return f'{self.name}'
    
# flask security --- USERS

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                       )
"""
create migration
----------------------
py manage.py db upgrade
py manage.py db upgrade
"""

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(133)) # flask-bcrypt for heshing
    active = db.Column(db.Boolean)

    def __repr__(self):
        return f'{self.name}'
    
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'{self.name}'

