#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     15/03/2016
# Copyright:   (c) Administrator 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def TotalIncome(gender):
    from ReadFile import ReadData
    the_data = ReadData.personal
    male_income = 0
    female_income = 0
    length = len(the_data)

    for element in range (0,length):
        if the_data[element][1] == "F":
            female_income += int(the_data[element][5])
            print(female_income)
        elif the_data[element][1] == "M":
            male_income += int(the_data[element][5])
            print(male_income)


    if (gender == 'Female'):
        print(female_income)
    elif (gender == 'Male'):
        print(male_income)

TotalIncome("Female")
