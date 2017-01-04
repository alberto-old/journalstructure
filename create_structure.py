#!/usr/bin/python
import datetime
import sys

def find_first_day_of_year (year):
    """ Find first day of year which is also in the ISO year """
    current = datetime.date (year, 1, 1)
    while current.isocalendar()[0] != year:
        current += datetime.timedelta (days=1)
    return current

def create_days_for_year (year):
    """ Create a list of days for the year passed as parameter """
    current = find_first_day_of_year (year)
    last  = datetime.date (year, 12, 31)
    days = []

    while current != last:
        days.append (current)
        current += datetime.timedelta(days=1)
    days.append(last)

    return days

def print_journal_day (day, current_week):
    """ Print a day of the journal """

    week_change = False
    week = day.isocalendar()[1]
    if week != current_week:
        # print week number, first and last days of the week
        first = day - datetime.timedelta (days=day.weekday())
        last = first + datetime.timedelta (days=6)
        print ("\n##### Week", week, "(", first.strftime("%d.%m"), last.strftime("%d.%m"), ")")

        week_change = True

    if day.day == 1:
        # print month if first day of the month
        print ("\n####", day.strftime("%B"))

    # print day
    print ("*", day.strftime("%a %d.%m.%Y"))

    if week_change:
        return current_week+1
    else:
        return current_week

def print_journal_days (days):
    """ Print a Journal using the days passed as parameter """
    print ("### Journal", days[0].year)
    current_week = 0
    for day in days:
        current_week = print_journal_day (day, current_week)

if len(sys.argv) == 2:
    days = create_days_for_year(int(sys.argv[1]))
    print_journal_days (days)
else:
    print ("Correct usage: python create_structure.py <YEAR>")
