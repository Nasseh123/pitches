from flask import render_template
from . import main
from ..models import Pitch

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message='Index Page'
    title = 'Home - Welcome to The Pitchpitches'
    return render_template('index.html',message=message,title=title)

@main.route('/pitch/<category>')
def movie(category):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('categories.html',category = category)