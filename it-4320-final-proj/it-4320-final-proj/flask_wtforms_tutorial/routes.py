from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash
from .forms import *
import numpy
import pandas as pd
import itertools
import csv


# returns true if there is no other reservation for that seat
def validate_choice(row, seat):
    data = pd.read_csv('reservations.csv', header=None, usecols=[1, 2], names=['row', 'seat'])
    data = data[data.row == row]
    data = data[data.seat == seat]
    if data.empty:
        return True
    else:
        return False


# generate reservation code
def create_reservation_code(first_name):
    string_1 = "INFOTC1040"
    new_list = []
    for f, b in itertools.zip_longest(first_name, string_1):
        if f:
            new_list.append(f)
        if b:
            new_list.append(b)
    return ''.join(new_list)


# add reservation to file
def add_reservation_to_file(first_name, row, seat, reservation_code):
    data = first_name+', '+str(row)+', '+str(seat)+", "+reservation_code+"\n"
    with open("reservations.csv", "a") as fp:
        fp.write(data)


# this function generates a csv reader and a reservation list based on reservations.csv
# input: csv file path
# output: list[list[str]] of reservation info
def get_reservations_list(filename):
    file = open(filename)
    type(file)
    reader = csv.reader(file)
    reservations_list = []
    for row in reader:
        reservations_list.append(row)
    file.close()
    return reservations_list


def generate_seating_charts(reservation_list):
    seating_chart = {}
    for i in range(0, 12):
        seating_chart[i] = ['O', 'O', 'O', 'O']
    for line in reservation_list:
        seating_chart[int(line[1])][int(line[2])] = "X"
    return seating_chart


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
    # posting data used for checking if statment in templete, allows for display for first page load, and submitted
    posting_data = False
    # get the form data
    form = ReservationForm()
    # if submit was selected, then a requests will have a post method
    if request.method == "POST" and form.validate_on_submit():
        posting_data = True

        # get form data
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        row_choice = int(request.form["row"])
        seat_choice = int(request.form["seat"])

        # make sure reservation isnt already done
        validated_choice = validate_choice(row_choice, seat_choice)
        # seat choice is available to be reserved, generate code and add to list
        if validated_choice:
            reservation_code = create_reservation_code(first_name)
            add_reservation_to_file(first_name, row_choice, seat_choice, reservation_code)

        # create seating chart list
        initial_reservations_list = get_reservations_list('reservations.csv')
        seating_chart = generate_seating_charts(initial_reservations_list)

        # make the render call
        return render_template("reservations.html", form=form, template="form-template", posting_data=posting_data,
                               first_name=first_name, last_name=last_name, row_choice=row_choice,
                               seat_choice=seat_choice, validated_choice=validated_choice, seating_chart=seating_chart)
    # post is false, first time templete is made
    return render_template("reservations.html", form=form, template="form-template", posting_data=posting_data)

