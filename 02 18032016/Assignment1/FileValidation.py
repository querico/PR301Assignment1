from ReadFile import ReadData
import re

__author__ = 'Rui Zheng'


class Validation (object):
    readData = ReadData()
    theFile = readData.personal
    length = len(theFile)

    for element in range(0,length):
        if re.match(r'[A-Z][0-9]{3}',theFile[element][0]):
            print(str(theFile[element][0]) + '----> ID Checked')
        else:
            newID = input(theFile[element][0] + " " + 'is incorrect ID, Please enter the Correct ID which content, '
                                                'a capital letter fellow by 3 digits  --->')
            theFile[element][0] = newID

    for element in range(0, length):
        if theFile[element][1] == "F" or theFile[element][1] == "M":
            print(str(theFile[element][1]) + '----> Gender Checked')
        else:
            newGender = input(theFile[element][1] + " " + 'is incorrect Gender, Please enter the Correct Gender,'
                                                    'M for Male and F for Female --->')
            theFile[element][1] = newGender

    for element in range(0, length):
        if re.match(r'[0-9]{2}',theFile[element][2]):
            print(str(theFile[element][2]) + '----> Age Checked')
        else:
            newAge = input(theFile[element][2] + " " + ' is incorrect Age, Please enter the Correct Age, 00 - 99 --->')
            theFile[element][2] = newAge

    for element in range(0, length):
        if re.match(r'[0-9]{3}',theFile[element][3]):
            print(str(theFile[element][3]) + '----> Sales Checked')
        else:
            newSales = input(theFile[element][3] + " " + "is incorrect Sales, please Enter a correct number"
                                                   " between 000 - 999 --->")
            theFile[element][3] = newSales

    for element in range(0, length):
        if theFile[element][4] == "Normal" or theFile[element][4] == "Overweight" or\
            theFile[element][4] == "Obesity" or theFile[element][4] == "Underweight":
            print(str(theFile[element][4]) + '----> BMI Checked')
        else:
            newBMI = input(theFile[element][4] + " " + 'is incorrect BMI, Please enter the Correct BMI,'
                                                    'Normal, Overweight, Obesity or Underweight --->')
            theFile[element][4] = newBMI

    for element in range(0,length):
        if re.match(r'[0-9]{2,3}[\n]', theFile[element][5]):
            print(str(theFile[element][5]) + "----> Income Checked")
        else:
            newIncome = input(theFile[element][5] + " " + "is incorrect Income, "
                                                          "Please enter the correct Income between 00 - 999 ---> ")
            theFile[element][5] = newIncome + '\n'



















