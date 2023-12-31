import csv
import datetime
import tabulate

# All dates in the format YYYY-MM-DD
CITIES = {"1": 'Chennai', "2": 'Mumbai', "3": 'Bangalore', "4": 'Delhi'}


def average(filtered_dataset):
    avgl=[0,0,0,0]
    day=[0,0,0,0]
    k=0
    
    
    for i in filtered_dataset:
     if k==0:
         k+=1
         continue
     else:
        if i[1]!='':
            avgl[0]+=float(i[1])
            day[0]+=1
            
        if i[2]!='':
            avgl[1]+=float(i[2])
            day[1]+=1
            
        if i[3]!='':
            avgl[2]+=float(i[3])
            day[2]+=1

        if i[4]!='':
            avgl[3]+=float(i[4])
            day[3]+=1
            
    rainfallavg=(avgl[3]/day[3])
    tempavg=(avgl[0]/day[0])
    tminavg=(avgl[1]/day[1])
    tmaxavg=(avgl[2]/day[2])
    return(tempavg,tminavg,tmaxavg,rainfallavg)


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
    print('4. Based on current year')
    print('5. Based on current season')
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

#predicton based on 10 day avg

def tendayavg(city):
     date=input('enter a date')
     for i in city:
         if i[0]==date:
             k=city.index(i)
     tenavg=city[k-5:k+6]
     print(tenavg)

     y=average(tenavg)
     return avg
     




     
# main function
def main():
    madras = read_dataset('Madras.csv')
    mumbai = read_dataset('Mumbai.csv')
    bangalore = read_dataset('Bangalore.csv')
    
    cities_list = {"1":madras, "2":mumbai,"3":bangalore}


    

    # TODO should be fit into a while loop

    ans='yes'       
    while ans=='yes':
     opt = main_menu()
     if opt == 1:
        print()
        city = choose_city()     # number 1 or 2 
        city = cities_list[city]  # list 
        fromdate, todate = fromtodates()

        print()
        res = filter_data(city, fromdate, todate)
        print(tabulate.tabulate(res, headers='firstrow', tablefmt='grid'))

     elif opt == 2:
        l=[]
        print()
        city = choose_city()
        city = cities_list[city]
        fromdate, todate = fromtodates()
        #calling the average function here
        res = filter_data(city, fromdate, todate)#tuple
        print()
        

        cityavg=average(res)
        l1=['avgtemp of the city','tminavg','tmaxavg','rainfallavg of the city']
        l2=list(cityavg)
        l.append(l1)
        l.append(l2)
        print(tabulate.tabulate(l, headers='firstrow', tablefmt='grid'))

        #cityavg= average(city)
        #print(tabulate.tabulate(cityavg, headers='firstrow', tablefmt='grid'))


     elif opt == 3:
        l=[]
        print()
        l1=['city','avgtemp of the city','tminavg','tmaxavg','rainfallavg of the city']
        l.append(l1)
        city1 = choose_city()
        
        ##doubt
        l3=list(city1)
        l.append(l3)
        ##

        
        city1 =  cities_list[city1]
        fromdate, todate = fromtodates()
        res = filter_data(city1, fromdate, todate)#tuple
        

        cityavg=average(res)
        
        l2=list(cityavg)

        l.append(l2)
        
        print(tabulate.tabulate(l, headers='firstrow', tablefmt='grid'))

        #city2 = choose_city()
        #city2 = CITIES[city2]

        #print()
        #fromdate, todate = fromtodates()

        # TODO display averages for both cities for the given time period
        
        #  city       |   tavg | tmin   | tmax   | prcp   |
        # +============+========+========+========+========+
        # | Chennai   |   24   | 19.7   | 27.7   | 0      |
        # +------------+--------+--------+--------+--------+
        # | Mumbai    |   23.8 | 21.5   | 27     | 15.7

     elif opt == 4:
        city = choose_city()
        city = cities_list[city]
        o=prediction_menu()
        if o==1:
           avg= tendayavg(city)
           

        
    ans=input('do you wish to analyse more:')

        # TODO options for each prediction menu


main()
