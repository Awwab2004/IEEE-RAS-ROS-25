def get_tomorrow(day, month, year):
    if day == 30:
        day = 1
        month += 1
    else:
        day += 1
    print(f"Day: {day} Month: {month} Year: {year}")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))
get_tomorrow(day, month, year)