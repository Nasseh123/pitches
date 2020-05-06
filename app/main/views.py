from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch
from flask_login import login_required,current_user
from ..models import User
from  ..import db,photos
from .forms import UpdateProfile,AddPitch

# views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message='Index Page'
    title = 'Home - Welcome to The Pitchpitches'
    # user=User.get_user(id)
    pitch=Pitch.get_all_pitch()
    return render_template('index.html',message=message,title=title,pitch=pitch)

@main.route('/pitch/<category>')
def pitch(category):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('categories.html',category = category)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    user_id=user.id
    pitches=Pitch.get_pitch(user_id)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches=pitches)

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
    
    form=UpdateProfile()

    if form.validate_on_submit():
        user.bio=form.bio.data

        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/pitch/<id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):  
    form=AddPitch()
    user=User.get_user(id)
    if form.validate_on_submit():
        title=form.title.data
        category=form.category.data
        description=form.description.data
        new_pitch=Pitch(title=title,category=category,description=description,user_id=user.id)

        new_pitch.save_pitch()
        return redirect(url_for('.index',id=user.id))
    title='New Pitch'
    return render_template('pitch.html',title = title, pitch_form=form,user=user)
