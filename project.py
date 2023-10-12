def yearavg():
  try:
    import csv
    city=input('enter the city')
    a=city+'.csv'
    f=open(a,'r',newline='')
    v=csv.reader(f)
    year=int(input('eneter the year'))
    k=0
    rf=0
    at=0
    count=0
    tcount=0
    for i in v:
     if k==0:
      k+=1
      continue
     else:
        b=i[0].split('-')
        if year==int(b[-1]) and i[-1]!='':
              rf+=float(i[-1])
              count+=1
        else:
             continue
        if year==int(b[-1]) and i[1]!='':
          at+=float(i[1])
          tcount+=1
    print('average rainfall of th year is',rf/count)
    print('average temprature of the year is',at/tcount)
  except:
         print('data invalid')
def yandmavg():
  try:
    import csv
    city=input('enter the city')
    a=city+'.csv'
    f=open(a,'r',newline='')
    v=csv.reader(f)
    year=int(input('eneter the year'))
    month=int(input('enter the month'))
    k=0
    rf=0
    at=0
    count=0
    tcount=0
    for i in v:
      for i in v:
       if k==0:
         k+=1
         continue
       else:
        b=i[0].split('-')
        if year==int(b[-1]) and int(b[-2])==month and i[-1]!='':
              rf+=float(i[-1])
              count+=1
        else:
             continue
        if year==int(b[-1]) and i[1]!='':
          at+=float(i[1])
          tcount+=1
    print('average rainfall of the month is',rf/count)
    print('average temprature of the month  is',at/tcount)
  except:
         print('try')
def date():
    try:
        import csv
        city=input('enter the city')
        a=city+'.csv'
        f=open(a,'r',newline='')
        date=input('enter date in the form(dd-mm-yyyy)')
        v=csv.reader(f)
        for i in v:
          if i[0]==date:
            print(i)
    except:
           print('try entering the date again')
def season():
      try:
         import csv
         city=input('enter the city')
         a=city+'.csv'
         f=open(a,'r',newline='')
         v=csv.reader(f)
         year=int(input('enter a year'))
         pre=0
         swm=0
         nem=0
         c1=0
         c2=0
         c3=0
         k=0
         for i in v:
          if k==0:
           k+=1
           continue
          else:
            b=i[0].split('-')
            if year==int(b[-1]):
              if int(b[1])>=0 and int(b[1])<=5 and i[-1]!='':
                        pre+=float(i[-1])
                        c1+=1
              elif int(b[1])>=6 and int(b[1])<=9 and i[-1]!='':
                     swm+=float(i[-1])
                     c2+=1
              elif  int(b[1])>=10 and int(b[1])<=12 and i[-1]!='':
                nem+=float(i[-1])
                c3+=1
         print('the rf average in the premonsoon season of the',year,':',pre/c1,'the rf average in the southwestmonsoon season of the',year,':',swm/c2,'the rf  the northeastmonsoon ',year,':',nem/c3)
      except:
            print('bye')
def rainyday():
    import csv
    city=input('enter the city')
    a=city+'.csv'
    f=open(a,'r',newline='')
    v=csv.reader(f)
    year=int(input('eneter the year'))
    month=int(input('enter the month'))
    k=0
    count=0
    for i in v:
      for i in v:
       if k==0:
         k+=1
         continue
       else:
        b=i[0].split('-')
        if year==int(b[-1]) and int(b[-2])==month and i[-1]!=''and int(float(i[-1]))>0:
              count+=1
        
        else:
             continue
    print(count)
    
ans='yes'       
while ans=='yes':
    print('welcome to ssr weather analysis unit')
    print('Available cities,1)Chennai,2)Mumbai,3)Banglore,4)Delhi')
    print('available cities:')
    print("1)To find a year's average enter 1")
    print('2)to find the avg of a month in a partiuclar year:')
    print('3)to check the data on a paticular date')
    print('4)to know the season average of a particular year enter option 4')
    print('5)to know the number of rainy days in a month of a particular year')
    opt=int(input('enter the option that you you want to venture:'))
    if opt==1:
       yearavg()
    if opt==2:
      yandmavg()
    if opt==3:
      date()
    if opt==4:
      season()
    if opt==5:
        rainyday()
    ans=input('do you wish to analyse more:')

    
    
