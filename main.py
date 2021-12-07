from flask import *
from public import *
from admin import *
from user import *

app=Flask(__name__)

app.secret_key='AG'

app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user,url_prefix='/user')

app.run(debug=True,port=5349)