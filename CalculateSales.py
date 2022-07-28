#Given cost matrix
def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix

#Calculates and returns the total sales
def calculate_sales(seating_chart_full,cost_matrix):
    total_sales = 0
    for x in range(12):
        for y in range(4):
            if seating_chart_full[x][y] == "X":
                total_sales += cost_matrix[x][y]
            else:
                total_sales += 0
    return total_sales

