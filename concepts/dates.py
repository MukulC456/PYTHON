# from library import function --> syntax

'''
# To get current date and time we use datetime library
from datetime import datetime

# the now function from datetime library returns date & time as a datetime library object.
current_date = datetime.now()

print(f"Today is {current_date}.")
# be default the format is yyyy-mm-dd for date and hrs:min:sec:millisec for time
'''

'''
from datetime import datetime,timedelta

today = datetime.now()
one_day = timedelta(days=1)
previous_day = today - one_day

print(f"Today is {today}.")
print(f"Previous day was {previous_day}.")
'''

'''
from datetime import datetime

today = datetime.now()
print(today)
print(f"Day: {today.day}")
print(f"Month: {today.month}")
print(f"Year: {today.year}")
print()                       # to create a blank line
print(f"Hours: {today.hour}")
print(f"Minutes: {today.minute}")
print(f"Seconds: {today.second}")
'''

from datetime import datetime,timedelta

birthday = input("When is your birthday (dd/mm/yyyy)?: ")
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")
print(f"Birthday: {birthday_date}")
one_day = timedelta(days=1)
previous_day = birthday_date - one_day
print(f"Day before birthday: {previous_day}")