from flask import Flask, escape, request ,render_template, url_for, flash, redirect, session, Response, jsonify
from forms import RegistrationForm, LoginForm,  UpdateAccountForm, WtinputForm1 ,WtoutputForm
import json
from flask_mysqldb import MySQL
import MySQLdb.cursors
from flask_bcrypt import Bcrypt
import MySQLdb
from flask_bootstrap import Bootstrap
from mysqlscripts import *
import numpy

app = Flask(__name__)

app.config['MYSQL_USER'] ='root or your ID'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'workouttracker'
app.config['MYSQL_CURSORCLASS'] ='DictCursor'

mysql = MySQL(app)
Bootstrap(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = ''

@app.route('/')
def index():
    return render_template('home.html')




@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
    return render_template('calendar.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html', title = 'About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(registerMySQL.format(form.email.data))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists!'
        else:
            cursor.execute(registerMySQL2.format(form.firstname.data, form.lastname.data, form.email.data, form.password.data))
            mysql.connection.commit()


            flash(f'Account created for {form.email.data}!','success')
            cursor.close

        return redirect(url_for('login'))

    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if 'loggedin' in session:
        form = UpdateAccountForm()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(loginMySQL.format(session['id']))
        account = cursor.fetchone()
        # Show the profile page with account info
        form.email.data = account['email']
        form.firstname.data = account['first_name']
        return render_template('account.html',title='Account', form=form)

    if form.validate_on_submit():
        user_email = form.email.data
        user_password = form.password.data
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(loginMySQL2.format(user_email, user_password))
        account = cursor.fetchone()
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['first_name'] = account['first_name']
            flash('Logged in successfully!')
            # return 'Logged in successfully!'
            return redirect(url_for('account'))

    return render_template('login.html', title = 'Login', form=form)




@app.route("/logout")
def logout():
    # logout_user()
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('first_name', None)
    return redirect(url_for('home'))

@app.route("/wtinput", methods=['GET', 'POST'])
def wtinput():
    form = WtinputForm1()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if not 'loggedin' in session:
        return redirect(url_for('login'))

    if form.submit.data and form.validate() and request.method == 'POST':
        cursor.execute(wtinputMySQL.format(session['id'], form.date.data))
        r = cursor.fetchone()
        if r is None:

            cursor.execute(wtinputMySQL2.format(form.date.data, session['id'], form.sleephours.data))
            mysql.connection.commit()

            cursor.execute(wtinputMySQL.format(session['id'], form.date.data))
            r = cursor.fetchone()


        print( r['log_number'])
        if (form.workoutname.data !=""):
            cursor.execute(wtinputMySQL4.format(form.workoutname.data))
            w = cursor.fetchone()

            if w is None:
                cursor.execute(wtinputMySQL5.format(form.workoutname.data, form.equipment.data, form.muscleMajor.data, form.muscleMinor.data))
                mysql.connection.commit()
            else:
                cursor.execute(wtinputMySQL6.format(form.equipment.data, form.muscleMajor.data, form.muscleMinor.data, form.workoutname.data))
                mysql.connection.commit()

            cursor.execute(wtinputMySQL4.format(form.workoutname.data))
            w = cursor.fetchone()
            cursor.execute(wtinputMySQL3.format(form.workouthours.data, form.set.data, form.rep.data, r['log_number'], form.weight.data, w['WorkoutTypeID']))
            mysql.connection.commit()


        cursor.execute(wtinputMySQL7.format(form.illness.data, form.fatigue.data,r['log_number']))
        mysql.connection.commit()


        if (form.fooddrinkname.data != ""):
            cursor.execute(wtinputMySQL8.format(form.fooddrinkname.data, form.amount.data, form.carb.data, form.protein.data, form.fat.data, r['log_number']))
            mysql.connection.commit()


        flash("=====================form WORKED========================")

        return render_template('wtinput.html', title = 'Workout Tracker Input', form = form)


    if form.add1.data and form.validate() and request.method == 'POST':

        cursor.execute(wtinputMySQL.format(session['id'], form.date.data))
        r = cursor.fetchone()
        if r is None:

            cursor.execute(wtinputMySQL2.format(form.date.data, session['id'], form.sleephours.data))
            mysql.connection.commit()
            cursor.execute(wtinputMySQL.format(session['id'], form.date.data))
            r = cursor.fetchone()

        cursor.execute(wtinputMySQL4.format(form.workoutname.data))
        w = cursor.fetchone()
        if w is None:
            cursor.execute(wtinputMySQL5.format
                           (form.workoutname.data, form.equipment.data, form.muscleMajor.data, form.muscleMinor.data))
            mysql.connection.commit()
        else:
            cursor.execute(wtinputMySQL6.format
                           (form.equipment.data, form.muscleMajor.data, form.muscleMinor.data, form.workoutname.data))
        cursor.execute(wtinputMySQL4.format(form.workoutname.data))
        w = cursor.fetchone()
        cursor.execute(wtinputMySQL3.format(form.workouthours.data, form.set.data,
                                       form.rep.data, r['log_number'], form.weight.data, w['WorkoutTypeID']))
        mysql.connection.commit()


        flash("=====================add1 WORKED========================")

        return render_template('wtinput.html', title = 'Workout Tracker Input', form = form)

    if form.add2.data and form.validate() and request.method == 'POST':



        cursor.execute(wtinputMySQL.format(session['id'], form.date.data))
        r = cursor.fetchone()
        if r is None:
            cursor.execute(wtinputMySQL2.format(form.date.data, session['id'], form.sleephours.data))
            mysql.connection.commit()
            cursor.execute(wtinputMySQL.format(session['id'], form.date.data))
            r = cursor.fetchone()

        cursor.execute(wtinputMySQL8.format(
        form.fooddrinkname.data, form.amount.data, form.carb.data, form.protein.data, form.fat.data, r['log_number']))
        mysql.connection.commit()
        flash("=====================add2 WORKED========================")

        return render_template('wtinput.html', title = 'Workout Tracker Input', form = form)


    return render_template('wtinput.html', title = 'Workout Tracker Input', form= form)



@app.route('/wtoutput', methods=['GET', 'POST'])
def wtoutput():
    form = WtoutputForm()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if not 'loggedin' in session:

        return redirect(url_for('login'))

    # if 'loggedin' in session and request.method == 'GET':
    cursor.execute(wtoutputMySQL4.format(session['id']))
    mysql.connection.commit()
    wtname = cursor.fetchall()
    if wtname is None:
        flash("\n\n======================No workout Name on User's record=======================")
        return redirect(url_for('wtinput'))

    choices =[]
    for i in range(0, len(wtname)):
        choices.append((wtname[i]['WorkoutName'], wtname[i]['WorkoutName']))
    form.nameSelect.choices = choices

    periodChoices =[(90, "Last 3 Months"), (30, "Last Month"), (7, "Last Week")]
    form.periodSelect.choices = periodChoices
    # print(form.periodSelect.data)

    cursor.execute(wtoutputMySQL.format(session['id'], form.periodSelect.data))
    wtoutputfetch = cursor.fetchall()
    cursor.execute(wtoutputMySQL2.format(session['id'], form.periodSelect.data))
    wtoutputfetch2 = cursor.fetchall()
    # cursor.execute(wtoutputMySQL3.format(session['id'], wtname['WorkoutTypeID']))
    cursor.execute(wtoutputMySQL3.format(session['id'], form.nameSelect.data, form.periodSelect.data))
    wtoutputfetch3 = cursor.fetchall()
    cursor.execute(wtoutputMySQL6.format(session['id'], form.periodSelect.data))
    wtoutputfetch6 = cursor.fetchall()
    cursor.execute(wtoutputMySQL7.format(session['id'], form.periodSelect.data))
    fetch6zip = cursor.fetchall()
    cursor.execute(wtoutputMySQL8.format(session['id'], form.periodSelect.data))
    wtoutputfetch8 = cursor.fetchall()

    if wtoutputfetch6[0]['avgCarb'] is None:
        flash(f"======================No Nutrition on record  for last {form.periodSelect.data} days=======================")
        return redirect(url_for('wtinput'))

    nutrition ={
        "avgCarb" : int(wtoutputfetch6[0]['avgCarb']),
        "avgProtein" : int(wtoutputfetch6[0]['avgProtein']),
        "avgFat": int(wtoutputfetch6[0]['avgFat'])
    }
    # nutrition2 = {
    #     "Carb": int(wtoutputfetch6[0]['carb']),
    #     "Protein": int(wtoutputfetch6[0]['protein']),
    #     "Fat": int(wtoutputfetch6[0]['fat'])
    # }

    # nutrition = json.dumps(nutrition)
    # print(nutrition)


    dates1 = []
    dates2 = []
    dates3 = []
    dates4 = []

    sleephours = []
    sumOfworkouthours =[]
    sumOfworkoutset = []
    sumOfworkoutsetNrep = []
    sumOfworkoutsetNrepNweight = []
    intensity = []
    carb =[]
    protein = []
    fat = []


    for i in range(0, len(wtoutputfetch)):
        dates1.append(wtoutputfetch[i]['log_date'].strftime('%Y-%m-%d'))
        sleephours.append(wtoutputfetch[i]['sleep_hours'])
    # print(dates1)
    # print(sleephours)
    for i in range(0, len(wtoutputfetch2)):
        dates2.append(wtoutputfetch2[i]['log_date'].strftime('%Y-%m-%d'))
        sumOfworkouthours.append(int(wtoutputfetch2[i]['workouthours']))
    # print(dates2)
    # print(sumOfworkouthours)
    for i in range(0, len(wtoutputfetch3)):

        dates3.append(wtoutputfetch3[i]['log_date'].strftime('%Y-%m-%d'))
        sumOfworkoutset.append(int(wtoutputfetch3[i]['totalsets']))
        sumOfworkoutsetNrep.append(int(wtoutputfetch3[i]['totalreps']))
        sumOfworkoutsetNrepNweight.append(int(wtoutputfetch3[i]['volume']))
        intensity.append(int(wtoutputfetch3[i]['intensity']))

    for i in range(0, len(wtoutputfetch8)):
        dates4.append(wtoutputfetch8[i]['logdate'].strftime('%Y-%m-%d'))
        carb.append(wtoutputfetch8[i]['carb'])
        protein.append(wtoutputfetch8[i]['protein'])
        fat.append(wtoutputfetch8[i]['fat'])

    print(dates4)
    print(carb)
    print(protein)
    print(fat)


    ren = render_template('wtoutput.html', form=form, nutrition = nutrition, fetch6zip= fetch6zip,
                               title='Workout Tracker Output', carb = carb, protein = protein, fat= fat,
                               dates1=dates1, dates2=dates2, dates4=dates4,
                               dates3=dates3, sleephours=sleephours, sumOfworkouthours=sumOfworkouthours,
                               sumOfworkoutset=sumOfworkoutset, sumOfworkoutsetNrep=sumOfworkoutsetNrep,
                               sumOfworkoutsetNrepNweight=sumOfworkoutsetNrepNweight, intensity=intensity)


    if form.validate_on_submit():
        # cursor.execute(wtoutputMySQL5, form.workoutname.data)
        # mysql.connection.commit()
        # wtname = cursor.fetchone()
        return ren

    return ren



@app.route("/account", methods=['GET', 'POST'])
def account():
    form = UpdateAccountForm()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if 'loggedin' not in session:
        return render_template('login.html', form=form)

    if form.validate_on_submit():

        # cursor.execute('SELECT * FROM wt_user WHERE id = %s', [session['id']])
        # print(accountMySQL2.format(form.age.data, form.gender.data, form.bodyweight.data, form.height.data, session['id']))
        print(form.age.data, form.gender.data, form.bodyweight.data, form.height.data, session['id'])
        cursor.execute(accountMySQL2.format
                       (form.age.data, form.gender.data, form.bodyweight.data, form.height.data, session['id']))
        mysql.connection.commit()
        flash("=====================Personal Information updated========================")
        return render_template('account.html', title='Account', form=form)

    cursor.execute(accountMySQL.format(session['id']))
    account = cursor.fetchone()

    # Show the profile page with account info
    form.email.data = account['email']
    form.firstname.data = account['first_name']
    form.age.data = account['age']
    form.gender.data = account['gender']
    form.bodyweight.data = account['weight_pound']
    form.height.data = account['height_cm']

    cursor.execute(accountMySQL3.format(session['id']))
    proteinAmount = cursor.fetchone()
    cursor.execute(accountMySQL4.format(session['id']))
    workoutdates = cursor.fetchone()
    notification1 = False
    if proteinAmount is not None and workoutdates is not None:
        if workoutdates['CL'] >= 3:
            # Men: Lean body mass = (0.32810 × W) + (0.33929 × H) − 29.5336
            # women: Lean body mass = (0.29569 × W) + (0.41813 × H) − 43.2933
            if account['gender'] =="female":
                womenLeanbodymass = ((0.32810 * account['weight_pound']) + (0.33929 * account['height_cm']) - 29.5336)*1000
                if (womenLeanbodymass*2.2) > proteinAmount["PA"]:
                    notification1 = True
            elif account['gender'] == "male":
                MenLeanbodymass = ((0.29569 * account['weight_pound']) + (0.41813 * account['height_cm']) - 43.2933)*1000
                if (MenLeanbodymass*2.2) > proteinAmount["PA"]:
                    notification1 = True





    return render_template('account.html', title='Account', form=form, notification1= notification1)



@app.route("/deletedate",methods=["POST","GET"])
def deletedate():
    if request.method == "POST":
        dateStr = request.form["dateStr"]

    cursor = mysql.connection.cursor()
    cursor.execute(calendarsettingMySQL2.format(session['id'], dateStr))
    mysql.connection.commit()

    # inputdate = request.form.get("value")
    print(dateStr)
    return redirect(url_for('login'))

@app.route("/livesearch",methods=["POST","GET"])
def livesearch():
    searchbox = request.form.get("text")
    # print(searchbox)
    if searchbox == "":
        return
    cursor = mysql.connection.cursor()
    cursor.execute(livesearchMySQL.format(searchbox))
    result = cursor.fetchall()
    # print(result)
    return jsonify(result)

@app.route("/livesearch2",methods=["POST","GET"])
def livesearch2():
    searchbox = request.form.get("text")
    # if searchbox == "":
    #     return
    # print(searchbox)
    cursor = mysql.connection.cursor()
    cursor.execute(livesearchMySQL2.format(searchbox))
    result = cursor.fetchone()
    # print(result)
    # print(jsonify(result))
    return jsonify(result)




@app.route("/calendarsetting",methods=["POST","GET"])
def calendarsetting():
    searchbox = request.form.get("text")
    cursor = mysql.connection.cursor()
    # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    # query = f"SELECT distinct log_date FROM tracker_log;"
    # query = "select word_eng from words where word_eng LIKE '{}%' order by word_eng".format(searchbox)#This is just example query , you should replace field names with yours
    cursor.execute(calendarsettingMySQL.format(session['id']))
    results = cursor.fetchall()
    data =[]
    for result in results:
        data.append({ "title" : result["WorkoutName"], "start" : result["log_date"].strftime('%Y-%m-%d')})
    print(data)
    app_json = json.dumps(data)
    # return jsonify(result)
    return app_json

if __name__ == '__main__':
    app.run(debug=True)
