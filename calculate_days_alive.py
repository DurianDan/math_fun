def check_leap(year:int):
    if year%4 == 0 or year%400 ==0 :
        return True
    else:
        return False

def  increase_one_day(day:int,month:int,leap:bool):
    days_of_months = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if leap:
        days_of_months[2] = 29
    if day < days_of_months[month]:
        day += 1
    elif day == days_of_months[month]:
        day = 1
        if month ==12:
            month = 1
        else:
            month += 1
    return day,month

def increase_one_date(day,month,year):
    if day==31 and month ==12:
        day,month = 1,1
        year += 1
    else:
        day,month = increase_one_day(day,month,check_leap(year))
    return day,month,year

def calculate_days_alive():
    day_born,month_born,year_born = map(int,input("Enter your birthday with the format day/month/year (Eg: 12/05/2003)\n").split("/"))
    current_day,current_month,current_year = map(int,input("Enter the current date with the format day/month/year (Eg: 15/07/2013)\n").split("/"))
    days_alive = 0
    
    while 1 ==1:
        day_born,month_born,year_born =  increase_one_date (day_born,month_born,year_born)
        days_alive += 1
        if day_born==current_day and month_born==current_month and year_born==current_year:
            break
    return days_alive

if __name__ == "__main__":
    print(calculate_days_alive())
