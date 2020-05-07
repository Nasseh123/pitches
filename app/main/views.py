from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Pitch,Comment

from flask_login import login_required,current_user
from ..models import User
from  ..import db,photos
from .forms import UpdateProfile,AddPitch,CommentInput
from datetime import datetime
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
    general="general"
    pickuplines="pickuplines"
    interviewpitch="interviewpitch"
    productpitch="productpitch"            
    promotionpitch="promotionpitch"
    return render_template('index.html',message=message,title=title,pitch=pitch,
    general=general,pickuplines=pickuplines,interviewpitch=interviewpitch,
    productpitch=productpitch,promotionpitch=promotionpitch)

@main.route('/pitch/<category>')
def pitch(category):

    # general="general"
    # pickuplines="pickuplines"
    # interviewpitch="interviewpitch"
    # productpitch="productpitch"            
    # promotionpitch="promotionpitch"

    
    
   
    pitches=Pitch.query.filter_by(category=category).all()
    pitchess=Pitch.query.filter_by(category=category).first()
    # pitchss=pitches.get_all_pitch()
    # catname=pitches.id
    # category=pitches.category
    # pitch_id=pitches.id

    pitcheses=Pitch.get_pitch_category(category)
    form=CommentInput()
    
    if form.validate_on_submit():
        description=form.description.data
        
        new_comment=Comment(description=description,upvote=0,downvote=0,pitch_id=pitchess.id)
        # SAVE COMENT
        new_comment.save_new_comment()
        return redirect(url_for('.pitch',category=pitcheses.category))

        # return redirect(url_for('.movie',id = movie.id ))
    #
    pitches=Pitch.get_pitch_category(category)

    return render_template('categories.html',category = category,pitches=pitches,form=form)

@main.route('/user/<uname>')
def profile(uname):
    general="general"
    pickuplines="pickuplines"
    interviewpitch="interviewpitch"
    productpitch="productpitch"            
    promotionpitch="promotionpitch"

    user = User.query.filter_by(username = uname).first()
    user_id=user.id
    pitches=Pitch.get_pitch(user_id)
    
    
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,pitches=pitches,general=general,pickuplines=pickuplines,interviewpitch=interviewpitch,
    productpitch=productpitch,promotionpitch=promotionpitch)

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
