from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	if not session.get('login_id') is None:

		return render_template('admin_home.html')

	else:
		return redirect(url_for('public.public_login'))

@admin.route('/admin_manage_sentiments',methods=['get','post'])
def admin_manage_sentiments():

	if not session.get('login_id') is None:

		data={}

		if 'submit' in request.form:

			gender=request.form['gender']
			age=request.form['age']
			oness=request.form['oness']
			ncism=request.form['ncism']
			cness=request.form['cness']
			aness=request.form['aness']
			eversion=request.form['eversion']
			pnality=request.form['pnality']
			q="INSERT INTO `sentiment_types`(`gender`,`age`,`openness`,`neuroticism`,`conscientiousness`,`agreeableness`,`extraversion`,`personality`)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%(gender,age,oness,ncism,cness,aness,eversion,pnality)
			insert(q)

			flash('ADDED')

			return redirect(url_for('admin.admin_manage_sentiments'))

		q="SELECT * FROM sentiment_types"
		data['sentiments']=select(q)

		if 'action' in request.args:
			action=request.args['action']
			sid=request.args['sid']
		else:
			action=None

		if action=='delete':
			q="DELETE FROM `sentiment_types` WHERE `sentiment_id`='%s'"%(sid)
			delete(q)

			flash('DELETED')

			return redirect(url_for('admin.admin_manage_sentiments'))

		if action=='update':
			q="SELECT * FROM sentiment_types WHERE `sentiment_id`='%s'"%(sid)
			data['upsenti']=select(q)

		if 'submits' in request.form:

			gender=request.form['gender']
			age=request.form['age']
			oness=request.form['oness']
			ncism=request.form['ncism']
			cness=request.form['cness']
			aness=request.form['aness']
			eversion=request.form['eversion']
			pnality=request.form['pnality']

			q="UPDATE `sentiment_types` SET `gender`='%s',`age`='%s',`openness`='%s',`neuroticism`='%s',`conscientiousness`='%s',`agreeableness`='%s',`extraversion`='%s',`personality`='%s' WHERE `sentiment_id`='%s'"%(gender,age,oness,ncism,cness,aness,eversion,pnality,sid)
			update(q)

			flash('UPDATED')

			return redirect(url_for('admin.admin_manage_sentiments'))


		return render_template('admin_manage_sentiments.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_view_users')
def admin_view_users():

	if not session.get('login_id') is None:

		data={}

		q="SELECT * FROM users"
		data['users']=select(q)

		return render_template('admin_view_users.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_user_report')
def admin_user_report():

	if not session.get('login_id') is None:

		data={}

		q="SELECT * FROM users"
		data['users']=select(q)

		return render_template('admin_user_report.html',data=data)

	else:

		return redirect(url_for('public.public_login'))


@admin.route('/admin_manage_posts')
def admin_manage_posts():

	if not session.get('login_id') is None:

		data={}

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS user_name FROM posts INNER JOIN users USING(user_id)"
		data['posts']=select(q)
	 	
		if 'action' in request.args:
			action=request.args['action']
			pid=request.args['pid']
		else:
			action=None

		if action=='remove':
			q="DELETE FROM `posts` WHERE `post_id`='%s'"%(pid)
			delete(q)

			flash('REMOVED')

			return redirect(url_for('admin.admin_manage_posts'))


		return render_template('admin_manage_posts.html',data=data)

	else:

		return redirect(url_for('public.public_login'))


@admin.route('/admin_view_comments')
def admin_view_comments():

	if not session.get('login_id') is None:

		data={}

		pid=request.args['pid']

		q="SELECT * FROM `comments` WHERE post_id='%s'"%(pid)
		data['comments']=select(q)

		return render_template('admin_view_comments.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_view_activities')
def admin_view_activities():

	if not session.get('login_id') is None:

		data={}

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS user_name FROM `activities` INNER JOIN users USING(user_id)"
		data['activity']=select(q)

		return render_template('admin_view_activities.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_view_feedback')
def admin_view_feedback():

	if not session.get('login_id') is None:

		data={}

		q="SELECT *,CONCAT(`first_name`,' ',`last_name`) AS user_name FROM `feedback` INNER JOIN users USING(user_id)"
		res=select(q)
		data['feedback']=res

		return render_template('admin_view_feedback.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_view_complaints',methods=['get','post'])
def admin_view_complaints():

	if not session.get('login_id') is None:

		data={}

		q="SELECT *,concat(first_name,' ',last_name) AS user_name FROM complaints INNER JOIN users USING (user_id)"
		res=select(q)
		data['complaints']=res

		i=1 
		for row in res:
			if 'replys'+str(i) in request.form:
				reply=request.form['reply'+str(i)]
				id=request.form['ids'+str(i)]
				q="UPDATE `complaints` SET `reply`='%s',`date`=CURDATE() WHERE complaint_id='%s'"%(reply,id)
				update(q)

				flash("success")

				return redirect(url_for("admin.admin_view_complaints"))

			i=i+1

		return render_template('admin_view_complaints.html',data=data)

	else:

		return redirect(url_for('public.public_login'))

@admin.route('/admin_view_reported_users')
def admin_view_reported_users():

	if not session.get('login_id') is None:

		data={}

		q="SELECT *,CONCAT(first_name,' ',last_name) AS user_name FROM `reports` INNER JOIN users USING(user_id)"
		res=select(q)
		data['reports']=res

		if 'action' in request.args:
			action=request.args['action']
			uid=request.args['uid']
			rid=request.args['rid']
		else:
			action=None

		if action=='block':
			q="UPDATE `reports` SET `status`='blocked' WHERE report_id='%s'"%(rid)
			update(q)
			q1="DELETE FROM `users` WHERE user_id='%s'"%(uid)
			delete(q1)

			flash('BLOCKED')

			return redirect(url_for('admin.admin_view_reported_users'))

		return render_template('admin_view_reported_users.html',data=data)

	else:

		return redirect(url_for('public.public_login'))
