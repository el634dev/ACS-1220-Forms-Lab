from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title',
        validators=[
            DataRequired(), 
            Length(min=3, max=80, message="Your message needs to be betweeen 3 and 80 chars")
        ])
    publish_date = DateField('Date Published', validators=[DataRequired()])
    author = QuerySelectField('Author', query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres', query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')

    def validate_title(form, field):
        if 'banana' in field.data:
            raise ValidationError('Title cannot contain the word banana')


class AuthorForm(FlaskForm):
    """Form to create an author."""
    # Fill out the fields in this class for:
    # - the author's name
    name = StringField('Author Name',
        validators=[
            DataRequired(),
            Length(min=4, max=80, message="Author's name needs to be between 4 and 80 characters")
    ])
    # - the author's biography (hint: use a TextAreaField)
    biography = TextAreaField('Author Biography', validators=[DataRequired()])
    # - a submit button
    submit = SubmitField('Submit')

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.
    pass


class GenreForm(FlaskForm):
    """Form to create a genre."""
    # Fill out the fields in this class for:
    # - the genre's name (e.g. fiction, non-fiction, etc)
    name = StringField('Genre Name', validators=[DataRequired()])
    # - a submit button
    submit = SubmitField('Submit')
