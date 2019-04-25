#!/usr/bin/env python3
"""
Author : jasongiles
Date   : 2019-04-20
Purpose: Rock the Casbah
"""

import argparse
import sys
import re



# --------------------------------------------------
def get_args():
    """get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'date', metavar='str', help='Give a date in format mm/dd/yyyy to see day of the week for that date')

    return parser.parse_args()


# --------------------------------------------------
def warn(msg):
    """Print a message to STDERR"""
    print(msg, file=sys.stderr)


# --------------------------------------------------
def die(msg='Something bad happened'):
    """warn() and exit with error"""
    warn(msg)
    sys.exit(1)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    date = args.date

    date_re = re.compile('(?P<month>\d{1,2})'  # month
                         '[/-]'  # separator
                         '(?P<day>\d{1,2})'  # day
                         '[/-]'  # separator
                         '(?P<year>\d{4})')  # year
    proper_date = date_re.match(date)

    leap_days = 0
    month_days = 0
    days_years = 0
    days = 0

    month_days_list = [31,28,31,30,31,30,31,31,30,31,31,31]

    if not proper_date:
        print('Date given "{}" not give date in proper format (mm/dd/yyyy)'.format(date))
    if proper_date:
        print(proper_date,proper_date.groups())
        #print(proper_date.group('year'))
        year = int(proper_date.group('year'))
        month = int(proper_date.group('month'))
        day = int(proper_date.group('day'))

        if int(month)>12:
            die('The month provided "{}" exceeds the number of months in the year'.format(month))
        if int(day)> int(month_days_list[month-1]):
            die(" The day provided '{}' exceeds the number of days in the month ".format(day))
        if year<=1582:
            die("The year chosen '{}' is prior to the start of Leap Years (1582) and things get complicated".format(year)+
                ' such as do you follow the Gregorian Calendar'+
                " or the Julian Calendar?")

        for num_years in range(1583,year): #maybe need +1?
            #print('hello',num_years)
            days_years += 365

        print('Number of days before anything:',days_years)
        #days_years = days_years+30
        #print('Number of days after adding 30 days...:', days_years)



        for leap_day in range(1583,int(year)+1):
            if int(leap_day) % 4==0:
                if int(leap_day)% 100==0 and int(leap_day)%400==0:
                    leap_days += 1
                    #print(leap_day)
                elif int(leap_day)%100==0:
                    leap_days = leap_days
                    #print(leap_day, 'this should not count')
                else:
                    leap_days += 1
        print('leap days:',leap_days)
        for month_amount in range(0,month-1):
            month_days = month_days+int(month_days_list[month_amount])
        print('days from start of year to month;',month_days)
        for days in range(0,int(day)):
            days +=1
        print(leap_days,'without calculating month/day')
        if month <=2 and day <28:
            leap_days = leap_days-1
        print(leap_days)
        total_days = days_years + month_days +days+1+leap_days
        print(total_days)
        #total_days = 737170
        if total_days%7==0:
            weekday = 'Mon'
        elif total_days%7==1:
            weekday = 'Tueday'
        elif total_days%7==2:
            weekday = 'Wed'
        elif total_days%7==3:
            weekday = 'Thur'
        elif total_days%7==4:
            weekday = 'Fir'
        elif total_days%7==5:
            weekday = 'Sat'
        elif total_days%7==6:
            weekday = "Sun"
        print('{}/{}/{} was a {}'.format(month,day,year,weekday))





# --------------------------------------------------
if __name__ == '__main__':
    main()
