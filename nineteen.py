# Project Euler Problem 19

def find_first_day_of_months(start_year, end_year):
    ''' Will find how many Sundays' fall on the first of the month
    between 1 Jan start_year - 31 Dec end_year
    '''
    sunday_count = 0

    start_day = 2 # 1 Jan 1901 is a Tuesday (want day % 7 = 0 to be Sunday)
    cur_day = start_day

    normal_days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    leap_year_days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]

    for year in xrange(start_year, end_year+1):
        if is_leap_year(year):
            days_in_month = leap_year_days_in_month
        else:
            days_in_month = normal_days_in_month

        for index, num_days in enumerate(days_in_month):
            if is_sunday(cur_day):
                sunday_count += 1
            print "asdYear: %d, Month: %d, DayOfWeek: %d" % (year, index+1, cur_day % 7)
            cur_day += num_days
            

    return sunday_count



def is_sunday(day):
    return day % 7 == 0

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print find_first_day_of_months(1901, 2000)