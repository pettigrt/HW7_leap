def leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    

#No error checking on input for leap year. Assume correct input
if __name__ == "__main__":
    year = input("Enter the year: ")
    try:
        if leap_year(int(year)):
            print(year, "is a leap year")
        elif not leap_year(int(year)):
            print(year, "is not a leap year")
    except ValueError:
        print("Input is not in the correct format")
        exit