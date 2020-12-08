from flask import Flask,render_template,redirect,url_for,flash
from register_form import *
from models import *
from flask_login import LoginManager,login_user,current_user,login_required,logout_user
from flask_socketio import SocketIO, send , join_room, leave_room
from time import localtime , strftime

app = Flask(__name__)
app.secret_key = 'aabbcc'

app.config['SQLALCHEMY_DATABASE_URI']='postgres://gvpadmsbjhmhtq:45e9b9eb09559da62c86809cb8bf3a38f389033a4e7c9923340cd1bed4febf0e@ec2-34-202-65-210.compute-1.amazonaws.com:5432/d6aa7kh92dbec7'
db=SQLAlchemy(app)

socketio = SocketIO(app)

Rooms = ['Clothing','Shoe wear','Beauty Products','Accessories']
usr = []


#Configure Flask Login
login = LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):
   return  User.query.get(int(id))


@app.route("/",methods=['GET','POST'])
def index():
    reg_form = Registration_form()

    if reg_form.validate_on_submit():
        fname_val = reg_form.firstname.data
        lname_val = reg_form.lastname.data
        username_val = reg_form.username.data
        password_val = reg_form.password.data
        contact_val = reg_form.contactno.data

        hashed_password = pbkdf2_sha256.hash(password_val)
        user = User(firstname=fname_val,lastname=lname_val,
             username=username_val,contactno=contact_val,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Registered Successfully. Please Login to Continue..",'success')
        return redirect(url_for('login'))

    return render_template("index1.html",form=reg_form)

@app.route("/login",methods=['GET','POST'])
def login():
    login_form = Login_form()
    if login_form.validate_on_submit():
        user_obj = User.query.filter_by(username=login_form.username.data).first()
        login_user(user_obj)
        display = "Welcome "+ current_user.firstname + " " + current_user.lastname
        #flash(display)
        #flash('Login Successful')
        return redirect(url_for('store'))

    return render_template('login.html',form=login_form)

@app.route("/store",methods=['GET','POST'])
def store():
    if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

    return render_template('index.html')


@app.route("/products",methods=['GET','POST'])
def products():
    if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

    return render_template('products.html')


@app.route("/order",methods=['GET','POST'])
def order():
    if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

    return render_template('order.html')


@app.route("/order-placed",methods=['GET','POST'])
def orderplace():
    if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

    return render_template('orderPlaced.html')

@app.route("/recommend",methods=['GET','POST'])
def recommend():
    if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

    return render_template('recommend.html')

@app.route("/dresses",methods=['GET','POST'])
def dresses():
    if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

    return render_template('dresses.html')

@app.route("/tops",methods=['GET','POST'])
def tops():
    if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

    return render_template('top.html')

@app.route("/jeans",methods=['GET','POST'])
def jeans():
    if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

    return render_template('jeans.html')

@app.route("/chat",methods=['GET','POST'])
def chat():
   #print(usr)
   if not current_user.is_authenticated:
        flash("Please Login to continue",'danger')
        return redirect(url_for('login'))


   #user_obj = User.query.filter_by(username=login_form.username.data).first()

   return render_template('chat.html',user=current_user.username,rooms=Rooms,
        fname=current_user.firstname,lname=current_user.lastname)



@app.route("/logout",methods=['GET'])
def logout():
    login_form = Login_form()
    #user_obj = User.query.filter_by(username=login_form.username.data).first()
    logout_user()
    #flash(display)
    flash("Logout Successful")
    return redirect(url_for('login'))
    #return "Logout Successful"


@socketio.on('message')
def meassage(data):
    #send(data)
    send({'msg' : data['msg'], 'username' : data['username'] , 'time_msg' : strftime("%d %b %Y %H:%M" , localtime()) },
        room=data['room'])
    #print(f"{data}")


@socketio.on('join')
def join(data):
    join_room(data['room'])
    send({'msg': data['username'] + " has joined the " + data['room'] + " room."}
        ,room=data['room'])


@socketio.on('leave')
def leave(data):
    leave_room(data['room'])
    send({'msg': data['username'] + " has left the " + data['room'] + " room."}
        ,room=data['room'])



if __name__== "__main__":
    socketio.run(app,debug=True)
