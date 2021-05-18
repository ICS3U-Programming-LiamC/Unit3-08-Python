#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: May 18, 2021
# This program determines whether the year is a leap
# year or not


# if the year is a leap year this gets called
def is_leap_year():
    print("{} is indeed a leap year!".format(year))


# if the year is not a leap year this gets called
def is_not_leap_year():
    print("{} is not a leap year".format(year))


# if the year is a leap year this gets called
def is_leap_year_neg():
    print("{}BCE is indeed a leap year!".format(abs(year)))


# if the year is not a leap year this gets called
def is_not_leap_year_neg():
    print("{}BCE is not a leap year".format(abs(year)))


# this is the fucntion that does everything
def leap_yearer():
    # get the year
    global year
    year = input("What year do you wish to know about: ")

    # see if it will arise an error if turned into an int
    try:
        year = int(year)

# IF THE YEAR IS NEGATIVE #########
        if (year < 0):
            # before leap years were instated
            if (year < -45):
                # make the year positive so that it wont say -yearBCE
                year = abs(year)
                print("{}BCE is before leap years were invented".format(year))
            # now see is the year is a leap year or not
            else:
                # divisible by 4
                if (year % 4 == 0):

                    # divisible by 100
                    if (year % 100 == 0):

                        # divisible by all
                        if (year % 400 == 0):
                            is_leap_year_neg()

                        # only divisible by 4 and 100
                        else:
                            is_not_leap_year_neg()

                    # only divisible by 4
                    else:
                        is_leap_year_neg()

                # not divisible by any
                else:
                    is_not_leap_year_neg()

# IF THE YEAR IS POSITIVE ##############
        else:
            # divisible by 4
            if (year % 4 == 0):

                # divisible by 100
                if (year % 100 == 0):

                    # divisible by all
                    if (year % 400 == 0):
                        is_leap_year()

                    # only divisible by 4 and 100
                    else:
                        is_not_leap_year()

                # only divisible by 4
                else:
                    is_leap_year()

            # not divisible by any
            else:
                is_not_leap_year()

    except ValueError:
        print("This is not a valid year")


if __name__ == "__main__":
    leap_yearer()
