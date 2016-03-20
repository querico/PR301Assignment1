import cmd
from texttable import Texttable
import pickle

__author__ = 'Rui Zheng'
# -------------------------------------------------------------------------------
# Name:        Assignment 1 data import and analysis
# Purpose:     PR301 - Assignment 1
# Author:      Rui Zheng
# Created:     10/03/2016
# -------------------------------------------------------------------------------

# this is the Controller Class
class Controller(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "$$$"
        self.error = 0
    print("Welcome to the data collecting app \n"
        "Need Help please >>>help<<< command \n"
        "it will bring you useful information ")


    @staticmethod
    def do_about(command):
        """
        this about command shows user some information about this application
        """
        print("Welcome to the data collecting ap \n" +
              "This application is created for collection \n" +
              "data from a file and to display relationship  \n"
              "between data that relevant")

    def do_help(self, command):
        """
        this help command shows user all the command available
        """
        print("About command: shows information about this app \n" +
              "help command: shows all command for this app \n" +
              '-------------------------------------------------------------------\n'
              "readFile command: for user to select a file and store in memory \n"
              '-------------------------------------------------------------------\n'
              "display command: for user to display the row data \n"
              '-------------------------------------------------------------------\n'
              "validate command: for user to validate the inputted data \n"
              '-------------------------------------------------------------------\n'
              "displayChart command: for user to display the 2D chart \n"
              '-------------------------------------------------------------------\n'
              "display!@# Command: for used for display the character sheet \n"
              '-------------------------------------------------------------------\n'
              "save Command: is used for save the data\n"
              '-------------------------------------------------------------------\n')

    @staticmethod
    def do_readFile(self):
        """
         will let user to read file from local device
        :return: file data
        """
        from ReadFile import OpenFile


    @staticmethod
    def do_display(self):
        from ReadFile import ReadData
        file = ReadData()
        theRecord = file.personal
        recode_size = len(theRecord)
        t = Texttable()

        for element in range(0,recode_size):
            t.add_row(theRecord[element])
            t.header(['ID', 'Gender', 'Age', 'Sales', 'BMI', 'Income'])
        print(t.draw())

    @staticmethod
    def do_validate(self):
        from FileValidation import Validation
        print('Done')

    @staticmethod
    def do_save(file_name):
        """
        """
        try:
            if file_name == "":
                raise InvalidActionError(
                    "Please Enter a File Name"
                )
            else:
                from FileValidation import Validation
                file_data = Validation.theFile
                with open(file_name + ".pickle", 'wb')as save_file:
                    pickle.dump(file_data, save_file)
                print(
                    "Verified file saved as " + file_name + ".pickle"
                )
        except InvalidActionError as err:
            print(err)

    def do_quit(self):
        """
        Quit from my CMD
        :return: True
        """

        print("Quitting ......")
        return True


class InvalidActionError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr("Invalid Action: " + self.value)


if __name__ == '__main__':
    quitter = Controller()
    quitter.cmdloop()
