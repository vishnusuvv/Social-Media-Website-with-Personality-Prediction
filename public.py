from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def public_home():
	session.clear()
	return render_template('public_home.html')

@public.route('/public_login',methods=['get','post'])
def public_login():

	session.clear()

	if 'submit' in request.form:
		uname=request.form['uname']
		pword=request.form['pword']
		q="SELECT * FROM `login` WHERE `username`='%s' AND PASSWORD='%s'"%(uname,pword)
		res=select(q)

		if res:
			login_id=res[0]['login_id']
			session['login_id']=login_id

			if res[0]['usertype']=='admin':

				flash('WELCOME ADMIN')

				return redirect(url_for('admin.admin_home'))

			if res[0]['usertype']=='user':

				q="SELECT * FROM `users` WHERE `login_id`='%s'"%(login_id)
				ress=select(q)

				if ress:

					session['uid']=ress[0]['user_id']

					flash('WELCOME USER')

					return redirect(url_for('user.user_home'))

		else:

			flash('INVALID USERNAME OR PASSWORD')
				
	return render_template('public_login.html')

@public.route('/user_registration',methods=['get','post'])
def user_registration():

	if 'submit' in request.form:
		uname=request.form['uname']
		pword=request.form['pword']
		fname=request.form['fname']
		lname=request.form['lname']
		gender=request.form['gender']
		dob=request.form['dob']
		phone=request.form['phone']
		email=request.form['email']
		q="INSERT INTO `login`(`username`,`password`,`usertype`)VALUES('%s','%s','user')"%(uname,pword)
		id=insert(q)
		q1="INSERT INTO `users`(`login_id`,`first_name`,`last_name`,`gender`,`dob`,`phone`,`email`)VALUES('%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,gender,dob,phone,email)
		insert(q1)

		flash("REGISTRATION SUCCESSFULL")

		return redirect(url_for('public.public_login'))

	return render_template('user_registration.html')