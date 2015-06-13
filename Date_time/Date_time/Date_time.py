import datetime
current_time=datetime.datetime.now().time()
current_date=datetime.date.today()
#print(current_date)
#print(current_date.day)
#print(current_date.month)
#print(current_date.year)
#i=current_date.day
#print (i)
#formatting date month year
#print(current_date.strftime('%d-%b-%Y'))
#print(current_date.strftime('Please attend our event %a, %B %d in the year %Y'))
#birthdate=input('Enter your birth date')
#birthdate=datetime.datetime.strptime(birthdate,'%d/%m/%y').date()
#print(birthdate)
#print(birthdate.strftime('Please attend our event %a, %B %d in the year %Y'))
#difference=current_date-birthdate
#print(difference.days)
#print(difference.days/365)
#print(current_time.strftime('%I:%M:%S'))
print(current_time)
birth_time=input('Enter your birth time')
birth_time=datetime.datetime.strptime(birth_time,'%H:%M:%S').time()
print(birth_time)
difference=current_time-birth_time
print(difference)
