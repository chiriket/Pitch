from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import Pitch, User, Role
# from .. import db,photos
from . import main
from .forms import PitchForm,UpdateProfile

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = "Minute Pitch"

    return render_template('index.html',title = title)


    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' <in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))

@main.route('/pitches/<category>')
def pitches(category):
    pitches = Pitch.query.filter_by(category = category).all()

    return render_template("pitches.html", pitches = pitches, category = category)






@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    new_pitch = None

    if form.validate_on_submit():
        pitch_category = form.category.data
        pitch = form.pitch.data
        
        new_pitch = Pitch(category = pitch_category, pitch = pitch, user = current_user)

        new_pitch.save_pitch()

        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html',title = title, pitch_form = form, new_pitch=new_pitch)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
@login_required
def pitch(id):
    
    my_pitch = Pitch.query.get(id)
    comment_form = CommentsForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comments(comment_content = comment_data, pitch_id = id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)

    up_likes = UpVote.get_votes(id)
    down_likes = DownVote.get_downvotes(id)

    title = 'Comment | One Minute Pitch'
    return render_template('pitches.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title, likes = up_likes, dislikes=down_likes)
