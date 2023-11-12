import csv
import datetime
import tabulate

# All dates in the format YYYY-MM-DD
CITIES = {"1": 'Chennai', "2": 'Mumbai', "3": 'Bangalore', "4": 'Delhi'}


def average(filtered_dataset):
    pass
    # TODO entire function


# filtering records based on dates
def filter_data(dataset, fromdate, todate):
    filtered_data = []
    fromdate = datetime.datetime.strptime(fromdate, '%Y-%m-%d').date()
    todate = datetime.datetime.strptime(todate, '%Y-%m-%d').date()

    for row in dataset[1:]:
        rowdate = datetime.datetime.strptime(row[0], '%Y-%m-%d').date()
        if fromdate <= rowdate <= todate:
            filtered_data.append(row)

    filtered_data = [dataset[0]] + filtered_data

    return filtered_data


# read datasets and return data as a nested list
def read_dataset(filename):
    f = open(filename, newline='')
    return list(csv.reader(f))


# first menu presented to user
def main_menu():
    print('=' * 20)
    print('Welcome to SSR weather analysis unit')
    print('=' * 20, '\n')
    print('1. City Data')
    print('2. City Average')
    print('3. Comparison between cities')
    print('4. Prediction for a city')
    opt = int(input('Enter option (1-3):'))
    return opt


# prediction menu
def prediction_menu():
    print('1. Based on 10 days average')
    print('2. Based on current month')
    print('3. Based on 3 months average')
    print('3. Based on current year')
    print('4. Based on current season')
    opt = int(input('Enter option(1-4):'))
    return opt


# Choose city menu
def choose_city():
    for key in CITIES.items():
        print(". ".join(key))
    city = input('Choose city (1-4): ')
    return city


# Choose from and to dates
def fromtodates():
    fromdate = input('Enter from date (yyyy-mm-dd):')
    todate = input('Enter to date (yyyy-mm-dd):')
    return fromdate, todate


# main function
def main():
    madras = read_dataset('Madras.csv')
    mumbai = read_dataset('Mumbai.csv')
    bangalore = read_dataset('Bangalore.csv')

    opt = main_menu()
    if opt == 1:
        print()
        city = choose_city()
        city = CITIES[city]
        fromdate, todate = fromtodates()

        print()
        res = filter_data(madras, fromdate, todate)
        print(tabulate.tabulate(res, headers='firstrow', tablefmt='grid'))

    elif opt == 2:
        print()
        city = choose_city()
        city = CITIES[city]
        fromdate, todate = fromtodates()

        # TODO call the average function here

    elif opt == 3:
        print()
        city1 = choose_city()
        city1 = CITIES[city1]

        print()
        city2 = choose_city()
        city2 = CITIES[city2]

        print()
        fromdate, todate = fromtodates()

        # TODO display averages for both cities for the given time period

    elif opt == 4:
        print()
        city = choose_city()
        city = CITIES[city]
        print()
        prediction_menu()

        # TODO options for each prediction menu


main()
