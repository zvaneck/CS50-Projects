def main():

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    date = get_date("Date: ", months)
    print(date)

def get_date(prompt, list):

    while True:
        try:
            x = input(prompt).strip()
            if "/" in x:
                format = x.split("/")
                if len(format) == 3:
                    if len(format[0]) <= 2 and len(format[1]) <= 2 and len(format[2]) == 4:
                        day = int(format[1])
                        month = int(format[0])
                        year = int(format[2])
                        if day <= 31 and month <= 12:
                            return str(year).zfill(2) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            elif "," in x:
                format = x.replace(",", "").split(" ")
                if format[0].title() in list and len(format[1]) <= 2 and len(format[2]) == 4:
                    day = int(format[1])
                    month = list.index(format[0]) + 1
                    year = int(format[2])
                    if day <= 31 and month <= 12:
                        return str(year).zfill(2) + "-" + str(month).zfill(2) + "-" + str(day).zfill(2)
                    else:
                        pass
                else:
                    pass
            else:
                pass
        except ValueError:
            pass

main()