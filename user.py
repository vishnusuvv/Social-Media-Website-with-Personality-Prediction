from flask import *
from database import *
from predict import predict
import uuid

user=Blueprint('user',__name__)

@user.route('/user_home')
def user_home():
	return render_template('user_home.html')

@user.route('/user_search_friends',methods=['get','post'])
def user_search_friends():

	data={}

	q="SELECT *,CONCAT(`first_name`,'  ',`last_name`) AS user_name FROM `users` WHERE user_id!='%s'"%(session['uid'])
	ress=select(q)
	data['users']=ress

	if 'submit' in request.form:
		a=request.form['fname']
		user="%"+a+"%"
		q="SELECT *,CONCAT(`first_name`,'  ',`last_name`) AS user_name FROM `users` WHERE `first_name` LIKE '%s'"%(user)
		ress=select(q)
		data['users']=ress

	if 'action' in request.args:
		action=request.args['action']
		fid=request.args['fid']
	else:
		action=None

	if action=='request':

		q="SELECT * FROM `friends` WHERE `fid`='%s' AND `user_id`='%s'"%(fid,session['uid'])
		res=select(q)

		if res:

			flash("ALREADY REQUESTED")

		else:
			uid=session['uid']
			q="INSERT INTO `friends`(`user_id`,`fid`,`status`)VALUES('%s','%s','requested')"%(uid,fid)
			insert(q)

	return render_template('user_search_friends.html',data=data)

@user.route('/user_make_a_post',methods=['get','post'])
def user_make_a_post():

	data={}

	if 'submit' in request.form:

		title=request.form['title']
		
		content=request.form['content']
		image=request.files['image']
		titles=title+" "+content
		personality_type = predict(titles)
		path="static/posts/"+str(uuid.uuid4())+image.filename
		image.save(path)

		q="INSERT INTO `posts`(`user_id`,`title`,`post_content`,`date`,`status`,`image`,`personality`)VALUES('%s','%s','%s',CURDATE(),'pending','%s','%s')"%(session['uid'],title,content,path,personality_type)
		insert(q)

		return redirect(url_for('user.user_make_a_post'))

	q="SELECT * FROM posts WHERE user_id='%s'"%(session['uid'])
	res=select(q)
	data['posts']=res

	if 'action' in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM posts WHERE post_id='%s'"%(pid)
		res=select(q)
		data['uppost']=res

	if 'submits' in request.form:

		title=request.form['title']
		content=request.form['content']

		q="UPDATE `posts` SET `title`='%s',`post_content`='%s',`date`=CURDATE() WHERE `post_id`='%s'"%(title,content,pid)
		update(q)

		return redirect(url_for('user.user_make_a_post'))

	if action=='delete':
		q="DELETE FROM posts WHERE post_id='%s'"%(pid)
		delete(q)

		return redirect(url_for('user.user_make_a_post'))

	return render_template('user_make_a_post.html',data=data)

@user.route('/user_view_posts')
def user_view_posts():

	data={}

	q="SELECT *,CONCAT(`first_name`,' ',`last_name`)AS user_name FROM posts INNER JOIN users USING(user_id) WHERE `user_id`!='%s'"%(session['uid'])
	res=select(q)
	data['posts']=res

	return render_template('user_view_posts.html',data=data)

@user.route('/user_view_posts1')
def user_view_posts1():

	data={}

	q="SELECT *,CONCAT(`first_name`,' ',`last_name`)AS user_name FROM posts INNER JOIN users USING(user_id) WHERE `user_id`!='%s'"%(session['uid'])
	res=select(q)
	data['posts']=res

	return render_template('user_view_posts1.html',data=data)

	

@user.route('/user_make_comments',methods=['post','get'])
def user_make_comments():

	data={}

	pid=request.args['pid']
	data['pid']=pid

	if 'submit' in request.form:

		comment=request.form['comment']

		q="INSERT INTO `comments`(`post_id`,`user_id`,`comment`,`date_time`)VALUES('%s','%s','%s',NOW())"%(pid,session['uid'],comment)
		insert(q)

		return redirect(url_for('user.user_make_comments',pid=pid))

	q="SELECT *,CONCAT(users.`first_name`,' ',users.`last_name`) AS user_name FROM `comments` INNER JOIN `posts` USING(post_id) INNER JOIN users ON posts.user_id=users.`user_id` WHERE `posts`.`user_id`!=2"
	res=select(q)
	data['comment']=res

	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `comments` WHERE `comment_id`='%s'"%(cid)
		select(q)
		data['upcom']=res

	if 'submits' in request.form:
		comment=request.form['comment']
		q="UPDATE `comments` SET `comment`='%s',`date_time`=NOW() WHERE `comment_id`='%s'"%(comment,cid)
		update(q)

		return redirect(url_for('user.user_make_comments',pid=pid))

	if action=='delete':
		q="DELETE FROM comments WHERE comment_id='%s'"%(cid)
		delete(q)

		return redirect(url_for('user.user_make_comments',pid=pid))

	return render_template('user_make_comments.html',data=data)


@user.route('/user_share_activity',methods=['get','post'])
def user_share_activity():

	data={}

	q="SELECT * FROM `activities` WHERE `user_id`='%s'"%(session['uid'])
	res=select(q)
	data['activity']=res

	if 'submit' in request.form:

		uid=session['uid']
		activity=request.form['activity']
		q="INSERT INTO `activities`(`user_id`,`activity_details`,`date_time`)VALUES('%s','%s',NOW())"%(uid,activity)
		insert(q)

		return redirect(url_for('user.user_share_activity'))

	if 'action' in request.args:
		action=request.args['action']
		aid=request.args['aid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `activities` WHERE `activity_id`='%s'"%(aid)
		select(q)
		data['upact']=res

	if 'submits' in request.form:
		activity=request.form['activity']
		q="UPDATE `activities` SET `activity_details`='%s',`date_time`=NOW() WHERE `activity_id`='%s'"%(activity,aid)
		update(q)

		return redirect(url_for('user.user_share_activity'))

	if action=='delete':
		q="DELETE FROM activities WHERE activity_id='%s'"%(aid)
		delete(q)

		return redirect(url_for('user.user_share_activity'))


	return render_template('user_share_activity.html',data=data)

@user.route('/user_sent_feedback',methods=['get','post'])
def user_sent_feedback():

	data={}

	if 'submit' in request.form:

		uid=session['uid']
		feedback=request.form['feedback']

		q="INSERT INTO `feedback`(`user_id`,`feedback_details`)VALUES('%s','%s')"%(uid,feedback)
		insert(q)

		return redirect(url_for('user.user_sent_feedback'))

	q="SELECT * FROM feedback WHERE user_id='%s'"%(session['uid'])
	res=select(q)
	data['feedback']=res

	if 'action' in request.args:
		action=request.args['action']
		fid=request.args['fid']
	else:
		action=None

	if action=='update':
		q="SELECT * FROM `feedback` WHERE `feedback_id`='%s'"%(fid)
		res=select(q)
		data['upfeed']=res

	if 'submits' in request.form:

		feedback=request.form['feedback']

		q="UPDATE `feedback` SET `feedback_details`='%s' WHERE `feedback_id`='%s'"%(feedback,fid)
		update(q)

		return redirect(url_for('user.user_sent_feedback'))

	if action=='delete':
		q="DELETE FROM feedback WHERE feedback_id='%s'"%(fid)
		delete(q)

		return redirect(url_for('user.user_sent_feedback'))

	return render_template('user_sent_feedback.html',data=data)

@user.route('/user_sent_complaint',methods=['get','post'])
def user_sent_complaint():

	data={}

	if 'submit' in request.form:
		uid=session['uid']
		complaint=request.form['complaint']
		q="INSERT INTO `complaints`(`user_id`,`complaint`,`reply`,`date`)VALUES('%s','%s','pending',NOW())"%(uid,complaint)
		insert(q)

		return redirect(url_for('user.user_sent_complaint'))

	q="SELECT * FROM `complaints` WHERE user_id='%s'"%(session['uid'])
	res=select(q)
	data['complaints']=res

	if 'action' in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None

	if action=='delete':
		q="DELETE FROM complaints WHERE complaint_id='%s'"%(cid)
		delete(q)

		return redirect(url_for('user.user_sent_complaint'))

	return render_template('user_sent_complaint.html',data=data)

@user.route('/user_view_requests')
def user_view_requests():

	data={}

	uid=session['uid']
	q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS user_name FROM `friends` INNER JOIN users  USING (user_id) WHERE `status`='requested' AND fid='%s'"%(uid)
	res=select(q)
	data['friends']=res

	if 'action' in request.args:
		action=request.args['action']
		frid=request.args['frid']
	else:
		action=None

	if action=='accept':
		q="UPDATE `friends` SET `status`='accepted' WHERE `friend_id`='%s'"%(frid)
		update(q)

		flash("ACCEPTED")

		return redirect(url_for('user.user_view_requests'))

	return render_template('user_view_requests.html',data=data)

@user.route('/user_chat',methods=['get','post'])
def user_chat():

	data={}

	cid=request.args['cid']
	qry="select *,concat(first_name,' ',last_name) as name from users where user_id='%s'"%(cid)
	result=select(qry)
	data['name']=result

	if 'submit' in request.form:
		message=request.form['msg']
		q2="INSERT INTO chat(sender_id,receiver_id,message,`date_time`)VALUES('%s','%s','%s',NOW())"%(session['uid'],cid,message)
		insert(q2)
		return redirect(url_for('user.user_chat',cid=cid))

	q="SELECT * FROM chat WHERE (`sender_id`='%s' AND `receiver_id`='%s') OR (`sender_id`='%s' AND `receiver_id`='%s')"%(session['uid'],cid,cid,session['uid'])
	res=select(q)
	data['msg']=res

	return render_template('user_chat.html',data=data)

@user.route('/user_view_friends')
def user_view_friends():

	data={}

	q="SELECT *,CONCAT(`first_name`,'  ',`last_name`) AS user_name FROM `friends` INNER JOIN `users` USING (user_id) WHERE  `status`='accepted' AND user_id!='%s'"%(session['uid'])
	res=select(q)
	data['friends']=res

	return render_template('user_view_friends.html',data=data)