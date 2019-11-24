from app import app, db
import view
from posts.blueprint import posts
from models import *


app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    # db.create_all()
    # 
    # # Deleting all records:
    # Post.query.delete()
    # 
    # # Creating new ones:
    # p1 = Post(title='First post', body='First post body')
    # p2 = Post(title='Second post', body='Second post body')
    # p3 = Post(title='Third post 2000', body='Third post body')
    # p4 = Post(title='Fours post', body='Fours post body')
    # 
    # db.session.add(p1)
    # db.session.add(p2)
    # db.session.add(p3)
    # db.session.add(p4)
    # db.session.commit()  # note

    app.run()

