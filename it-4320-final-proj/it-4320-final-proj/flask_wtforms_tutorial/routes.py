from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from .forms import *
import numpy


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    #check if the request method is POST. POST method means that form data was submitted
    #So, if method is POST we can get the form data 
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            #if form option is "1" go to the admin page
            return redirect('/admin')
        else:
            #if form option is "2" go to the reservations page
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():

    form = AdminLoginForm()

    return render_template("admin.html", form=form, template="form-template")

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")

