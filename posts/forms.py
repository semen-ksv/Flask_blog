from wtforms import Form, StringField, TextAreaField

class PostForm(Form):
    title = StringField('Post title')
    body = TextAreaField('Post body')
    