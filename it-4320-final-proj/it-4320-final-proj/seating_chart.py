import csv
#from wsgi import app


#reading reservations list as csv

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

# this function generates seating charts by availability, current reservations and price
# input: list[list[str]] of reservation info
# output:  current reservation chart: dict[int, dict[int, str]], chart by availability: dict[int, list[str]], chart by price:  dict[int, list[int]]

def generate_seating_charts(reservation_list):
    seating_chart_full = {}
    seating_chart_basic = {}
    seating_chart_prices = {}
    for i in range(0, 12):
        seating_chart_full[i] = ({1: "empty                   ", 2: "empty                   ", 3: "empty                    ", 4: "empty                   "})  #spaces are to make printed chart more readable  - replace 'empty' with empty list objects for consistency.
        seating_chart_basic[i] = ['O', 'O', 'O', 'O']
        seating_chart_prices[i] = [100, 75, 50, 100]
    for line in reservation_list:
        seating_chart_full[int(line[1])][int(line[2]) + 1] = [line[0], line[3]] # only explanation for zero's in the reservation numbers is if indexing starts at 0 - converting each index to +1 when referencing seat keys
        seating_chart_basic[int(line[1])][int(line[2])] = "X"
    return seating_chart_full, seating_chart_basic, seating_chart_prices

def print_seating_chart(chart):
    for row in chart.values():
        print(row)

def get_seat_info(int, int2, seating_chart): #returns info for seat specified in arguments
    print(seating_chart[int -1][int2])

def show_reservations(res_list):
    for row in res_list:
        print(row)




#tests functionality of methods, prints each version of seating chart
if __name__ == "__main__":

    initial_reservations_list = get_reservations_list('reservations.csv')
    seating_chart, seating_chart_basic, seating_chart_prices = generate_seating_charts(initial_reservations_list)
    print("initial reservations:")
    show_reservations(initial_reservations_list)

    print("\nseating chart w/ customer info:\n")
    print_seating_chart(seating_chart)
    print("\nseating chart with seat-availability:")
    print_seating_chart(seating_chart_basic)
    print("\nseating chart by price:")
    print_seating_chart(seating_chart_prices)

    print('\ntesting reference seat info: row 1, seat 2 ->')
    get_seat_info(1, 2)

    #@app.route("/reservations")
    #def display_reservations():