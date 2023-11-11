import csv
madras=open('Chennai.csv','r',newline='')
mumbai=open('Mumbai.csv','r',newline='')
banglore=open('Bangalore.csv','r',newline='')
mas=csv.reader(madras)
mum=csv.reader(mumbai)
bng=csv.reader(banglore)
def filter(file,fromdate,todate):
    l=[]
    datefrom,monthfrom,yearfrom=fromdate.split('-')
    dateto,monthto,yearto=todate.split('-')
    for i in file:
        b=i[0].split('-')
        if yearfrom==b[-1]:
            l.append(i)
    return l 
p=filter(mas,'01-01-1990','31-12-1990')
print(p)


