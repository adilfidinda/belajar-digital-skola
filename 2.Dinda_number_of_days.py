isKabisat = {"1" : 31, "2" : 29, "3" : 31, "4" : 30, "5" : 31, "6" : 30, 
             "7" : 31, "8" : 31, "9" : 30, "10" : 31, "11" : 30, "12" : 31}

isNotKabisat = {"1" : 31, "2" : 28, "3" : 31, "4" : 30, "5" : 31, "6" : 30, 
                "7" : 31, "8" : 31, "9" : 30, "10" : 31, "11" : 30, "12" : 31}
                
print("\nPlease enter date with format year-month-day e.g 2021-03-14")
date1 = input("Date 1 : ").split("-")
year1, month1, day1 = date1
date2 = input("Date 2 : ").split("-")
year2, month2, day2 = date2

number_of_month = len(isKabisat.keys())
number_of_days = 0
error_message = ""

years = abs(int(year2) - int(year1))
months = abs(int(month2) - int(month1))
days = abs(int(day2) - int(day1)) + 1

def isKabisatOrNot() :
    if int(year1) % 4 == 0 or int(year2) % 4 == 0 :
        year = isKabisat
    else :
        year = isNotKabisat
    return year

def isKabisatOrNot2(y) :
    if int(y) % 4 == 0:
        year = isKabisat
    else :
        year = isNotKabisat
    return year

if int(year1) > int(year2) :
    error_message = "Invalid year input. Year 1 must older than year 2"
    print(error_message)
if int(month1) > number_of_month or int(month2) > number_of_month or int(month1) <= 0 or int(month2) <= 0 :
    error_message = "Invalid Month Input. There are just 12 months in a year"
    print(error_message)
elif years == 0 and int(month1) > int(month2) :
    error_message = "Invalid month input. Month 1 must older than month 2"
    print(error_message)
elif isKabisatOrNot()[str(month1.strip("0"))] < int(day1) or isKabisatOrNot()[str(month2.strip("0"))] < int(day2) or int(day1) <= 0 or int(day2) <= 0 :
    error_message = "Invalid Day Input"
    print(error_message)

if error_message == "" :
    if years == 0 and  months == 0 : #ini kalo tahun sama bulannya sama
        number_of_days = days
    elif years == 0 : # ini kalo tahunnya sama aja
        for m in range(int(month1), int(month2) + 1) :
            if m == int(month1) :
                number_of_days = isKabisatOrNot()[str(m)] - int(day1) + 1
            elif m == int(month2) :
                number_of_days += int(day2)
            else :
                number_of_days += isKabisatOrNot()[str(m)]
    else : 
        for y in range(int(year1), int(year2) + 1) :
            if y == int(year1) :                                                        # kalau y di tahun pertama         
                for m in range(int(month1), number_of_month + 1) :
                    if m == int(month1) :                                               # kalau m di bulan pertama
                        number_of_days = isKabisatOrNot2(y)[str(m)] - int(day1) + 1
                    else :                                                              # kalau m bukan di bulan pertama
                        number_of_days += isKabisatOrNot2(y)[str(m)]
            elif y != int(year1) and y != int(year2) :
                for m in range(1, number_of_month + 1) :
                    number_of_days += isKabisatOrNot2(y)[str(m)]
            else :
                for m in range(1, int(month2) + 1) :
                    if m != int(month2):
                        number_of_days += isKabisatOrNot2(y)[str(m)]
                    if m == int(month2):
                        number_of_days += int(day2)
    print(f'\nNumber of Days : {number_of_days}')