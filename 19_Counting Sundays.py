days=['SUN','MON','TUE','WED','THU','FRI','SAT']

def create_leap_year_calender(start_day,total_count):
    i=1
    j=start_day
    Odd_month=1
    Feb_month=0
    last_day = 0
    print("Leap year")
    current_date=0
    current_day=''

    for x in range(1,367):  #366 days in a Leap year

        if x == 32:
            #i=1
            Feb_month=1
        if x == 183 or x == 214: #if Month is July or August we are looping till 31 days
            Odd_month=1
        if x == 366:
            last_day = start_day + 2

        if j == 7:
            j = 0
            print(i, days[j])

            current_date = i
            current_day = days[j]
            if current_date == 1 and current_day == "SUN":
                print("Sunday came on 1st of month")
                total_count+=1

            j+=1
            i+=1
        else:
            print(i,days[j])
            current_date = i
            current_day = days[j]
            if current_date == 1 and current_day == "SUN":
                print("Sunday came on 1st of month")
                total_count+=1
            j+=1
            i+=1
        if i == 30 and Feb_month == 1:
            i=1
            Feb_month=0
            Odd_month=1
            print("------")
        if i == 32 and Odd_month == 1:
            i=1
            Odd_month = 0
            print("------")
        if i == 31 and Odd_month == 0:
            i=1
            Odd_month = 1
            print("------")
    print("----YEAR END-----")
    return last_day,total_count

def create_non_leap_year_calender(start_day,total_count):
    i=1
    j=start_day
    Odd_month=1
    Feb_month=0
    last_day = 0

    current_date=0
    current_day=''

    for x in range(1,366): #365 days in a Non-Leap year

        if x == 32:
            #i=1
            Feb_month=1
        if x == 182 or x == 213:  #if Month is July or August we are looping till 31 days
            Odd_month=1
        if x == 365:
            last_day = start_day + 1
        if j == 7:
            j = 0
            print(i, days[j])

            current_date = i
            current_day = days[j]
            if current_date == 1 and current_day == "SUN":
                print("Sunday came on 1st of month")
                total_count+=1

            j+=1
            i+=1
        else:
            print(i,days[j])

            current_date = i
            current_day = days[j]
            if current_date == 1 and current_day == "SUN":
                print("Sunday came on 1st of month")
                total_count+=1
            j+=1
            i+=1
        if i == 29 and Feb_month == 1:
            i=1
            Feb_month=0
            Odd_month=1
            print("------")
        if i == 32 and Odd_month == 1:
            i=1
            Odd_month = 0  # April will have 30 days
            print("------")
        if i == 31 and Odd_month == 0:
            i=1
            Odd_month = 1 # May will have 31 days
            print("------")
    print("----YEAR END-----")
    return last_day,total_count

def checkYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":

    total_count=0
    start_day=2 # Day on 1 Jan 1901 was Tuesday, so Tuesday comes 2 in days list starting from Sunday as 0

    for year in range(1901,2001):  #starting from 1901 to 2000
        print("Year",str(year))

        if (checkYear(year)):
            print("Leap year",str(year))
            start_day,total_count=create_leap_year_calender(start_day,total_count)
            if start_day == 8:
                start_day = 1
            if start_day > 6 and start_day < 8:
                start_day = 0
        else:
            print("Not a leap year")
            start_day,total_count=create_non_leap_year_calender(start_day,total_count)
            if start_day > 6:
                start_day = 0

    print("Total times Sunday came on 1st date of month from year 1901 to year 2000 is",str(total_count))